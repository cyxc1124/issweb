import concurrent.futures
import socket
import a2s
import jinja2
from app import server_config
from flask import Blueprint, render_template

server_list = Blueprint('server_list', __name__, url_prefix='/server_list')

QUERY_TIMEOUT = 1


class ServerInfo(object):
    pass


def format_duration(total_seconds):
    total_seconds = int(total_seconds)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours > 0:
        return "{}h {}m".format(hours, minutes)
    elif minutes > 0:
        return "{}m {}s".format(minutes, seconds)
    else:
        return "{}s".format(seconds)


jinja2.filters.FILTERS['duration'] = format_duration


def list_server(server_tuple_list: list, info_type: str):
    servers_info = []
    servers_pool = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=14) as pool:
        for index in range(len(server_tuple_list)):
            servers_pool.append(pool.submit(a2s.info, server_tuple_list[index], timeout=QUERY_TIMEOUT))
    concurrent.futures.wait(servers_pool)
    for index in range(len(server_tuple_list)):
        if servers_pool[index].exception() is None:
            server_info = servers_pool[index].result()
            server_info.status = True
        else:
            server_info = ServerInfo()
            server_info.status = False
        server_info.info_id = index
        server_info.info_type = info_type
        server_info.info_ip = server_tuple_list[index][0]
        server_info.info_port = server_tuple_list[index][1]
        servers_info.append(server_info)
    return servers_info


@server_list.route("/other")
def list_other():
    return render_template("serverlist.html", title='合作服务器列表', infos=list_server(server_config.other, 'other')), 200


@server_list.route("/tuanzi")
def list_tuanzi():
    return render_template("serverlist.html", title='团子服务器列表', infos=list_server(server_config.tuanzi, 'tuanzi')), 200


@server_list.route("/xiaocao")
def list_xiaocao():
    return render_template("serverlist.html", title='小草服务器列表', infos=list_server(server_config.xiaocao, 'xiaocao')), 200


def retrieve_server(ip: str, port: int):
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        info_future = pool.submit(
            a2s.info, (ip, port), timeout=QUERY_TIMEOUT)
        players_future = pool.submit(
            a2s.players, (ip, port), timeout=QUERY_TIMEOUT)
    concurrent.futures.wait((info_future, players_future))

    info_except = info_future.exception()
    players_except = players_future.exception()

    if isinstance(info_except, socket.timeout) or isinstance(players_except, socket.timeout):
        return 'Server did not respond.', None, None
    elif isinstance(info_except, a2s.BrokenMessageError) or isinstance(players_except, a2s.BrokenMessageError):
        return 'Server sent a broken response.', None, None
    elif info_except is not None or players_except is not None:
        return 'Server error.', None, None

    info_res = info_future.result()
    players_res = players_future.result()
    return None, players_res, info_res


def server_handler(server: tuple):
    error_msg, players_res, info_res = retrieve_server(ip=server[0],
                                                       port=server[1])
    if error_msg:
        return render_template("serverinfo.html", status="Error",
                               error=error_msg), 200
    else:
        return render_template("serverinfo.html", status="Success",
                               info=info_res, players=players_res), 200


@server_list.route("/other/<int:num>")
def retrieve_other(num: int):
    if num < len(server_config.other):
        return server_handler(server_config.other[num])
    else:
        return render_template("serverinfo.html", status="Error",
                               error="Server error."), 200


@server_list.route("/tuanzi/<int:num>")
def retrieve_tuanzi(num: int):
    if num < len(server_config.tuanzi):
        return server_handler(server_config.tuanzi[num])
    else:
        return render_template("serverinfo.html", status="Error",
                               error="Server error."), 200


@server_list.route("/xiaocao/<int:num>")
def retrieve_xiaocao(num: int):
    if num < len(server_config.xiaocao):
        return server_handler(server_config.xiaocao[num])
    else:
        return render_template("serverinfo.html", status="Error",
                               error="Server error."), 200
