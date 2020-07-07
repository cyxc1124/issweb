import concurrent.futures
import socket
import a2s
import jinja2

from flask import Blueprint, render_template

xiaocaoserverlist = Blueprint('xiaocaoserverlist', __name__, url_prefix='/xiaocaoserverlist')

QUERY_TIMEOUT = 1


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


@xiaocaoserverlist.route("/")
def xiaocaolist():
    ip = ['119.188.247.66', '119.188.247.66', '119.188.247.66', '119.188.247.66', '119.188.247.66', '119.188.247.66',
          '119.188.247.66', '119.188.247.66', '119.188.247.66', '119.188.247.66']
    port = ['27101', '27111', '27121', '27131', '27141', '27151', '27161', '27171', '27181', '27191']

    servers_info = []
    for (info_ip, info_port) in zip(ip, port):
        info_port = int(info_port)
        try:
            server_info = a2s.info((info_ip, info_port), timeout=0.1)
        except socket.timeout as e:
            server_info = 'null'
        except a2s.BrokenMessageError as e:
            server_info = 'null'
        else:
            pass
        servers_info.append(server_info)
    return render_template("xiaocaoserverlist.html", infos=servers_info), 200


@xiaocaoserverlist.route("/27100")
def xiaocao1():
    ip = '119.188.247.66'
    port = '27101'
    port = int(port)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        info_future = pool.submit(
            a2s.info, (ip, port), timeout=QUERY_TIMEOUT)
        players_future = pool.submit(
            a2s.players, (ip, port), timeout=QUERY_TIMEOUT)
    concurrent.futures.wait((info_future, players_future))

    info_except = info_future.exception()
    players_except = players_future.exception()

    if isinstance(info_except, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="Server did not respond.", server=server_arg), 200
    elif isinstance(info_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response.", server=server_arg), 200
    elif info_except is not None:
        raise info_except

    info_res = info_future.result()

    if isinstance(players_except, socket.timeout):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server did not respond."), 200
    elif isinstance(players_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server sent a broken response."), 200
    elif players_except is not None:
        raise players_except

    players_res = players_future.result()

    return render_template("serverinfo.html", status="Success",
                           info=info_res, players=players_res), 200


@xiaocaoserverlist.route("/27110")
def xiaocao2():
    ip = '119.188.247.66'
    port = '27111'
    port = int(port)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        info_future = pool.submit(
            a2s.info, (ip, port), timeout=QUERY_TIMEOUT)
        players_future = pool.submit(
            a2s.players, (ip, port), timeout=QUERY_TIMEOUT)
    concurrent.futures.wait((info_future, players_future))

    info_except = info_future.exception()
    players_except = players_future.exception()

    if isinstance(info_except, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="Server did not respond.", server=server_arg), 200
    elif isinstance(info_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response.", server=server_arg), 200
    elif info_except is not None:
        raise info_except

    info_res = info_future.result()

    if isinstance(players_except, socket.timeout):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server did not respond."), 200
    elif isinstance(players_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server sent a broken response."), 200
    elif players_except is not None:
        raise players_except

    players_res = players_future.result()

    return render_template("serverinfo.html", status="Success",
                           info=info_res, players=players_res), 200


@xiaocaoserverlist.route("/27120")
def xiaocao3():
    ip = '119.188.247.66'
    port = '27121'
    port = int(port)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        info_future = pool.submit(
            a2s.info, (ip, port), timeout=QUERY_TIMEOUT)
        players_future = pool.submit(
            a2s.players, (ip, port), timeout=QUERY_TIMEOUT)
    concurrent.futures.wait((info_future, players_future))

    info_except = info_future.exception()
    players_except = players_future.exception()

    if isinstance(info_except, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="Server did not respond.", server=server_arg), 200
    elif isinstance(info_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response.", server=server_arg), 200
    elif info_except is not None:
        raise info_except

    info_res = info_future.result()

    if isinstance(players_except, socket.timeout):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server did not respond."), 200
    elif isinstance(players_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server sent a broken response."), 200
    elif players_except is not None:
        raise players_except

    players_res = players_future.result()

    return render_template("serverinfo.html", status="Success",
                           info=info_res, players=players_res), 200


@xiaocaoserverlist.route("/27130")
def xiaocao4():
    ip = '119.188.247.66'
    port = '27131'
    port = int(port)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        info_future = pool.submit(
            a2s.info, (ip, port), timeout=QUERY_TIMEOUT)
        players_future = pool.submit(
            a2s.players, (ip, port), timeout=QUERY_TIMEOUT)
    concurrent.futures.wait((info_future, players_future))

    info_except = info_future.exception()
    players_except = players_future.exception()

    if isinstance(info_except, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="Server did not respond.", server=server_arg), 200
    elif isinstance(info_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response.", server=server_arg), 200
    elif info_except is not None:
        raise info_except

    info_res = info_future.result()

    if isinstance(players_except, socket.timeout):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server did not respond."), 200
    elif isinstance(players_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server sent a broken response."), 200
    elif players_except is not None:
        raise players_except

    players_res = players_future.result()

    return render_template("serverinfo.html", status="Success",
                           info=info_res, players=players_res), 200


@xiaocaoserverlist.route("/27140")
def xiaocao5():
    ip = '119.188.247.66'
    port = '27141'
    port = int(port)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        info_future = pool.submit(
            a2s.info, (ip, port), timeout=QUERY_TIMEOUT)
        players_future = pool.submit(
            a2s.players, (ip, port), timeout=QUERY_TIMEOUT)
    concurrent.futures.wait((info_future, players_future))

    info_except = info_future.exception()
    players_except = players_future.exception()

    if isinstance(info_except, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="Server did not respond.", server=server_arg), 200
    elif isinstance(info_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response.", server=server_arg), 200
    elif info_except is not None:
        raise info_except

    info_res = info_future.result()

    if isinstance(players_except, socket.timeout):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server did not respond."), 200
    elif isinstance(players_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server sent a broken response."), 200
    elif players_except is not None:
        raise players_except

    players_res = players_future.result()

    return render_template("serverinfo.html", status="Success",
                           info=info_res, players=players_res), 200


@xiaocaoserverlist.route("/27150")
def xiaocao6():
    ip = '119.188.247.66'
    port = '27151'
    port = int(port)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        info_future = pool.submit(
            a2s.info, (ip, port), timeout=QUERY_TIMEOUT)
        players_future = pool.submit(
            a2s.players, (ip, port), timeout=QUERY_TIMEOUT)
    concurrent.futures.wait((info_future, players_future))

    info_except = info_future.exception()
    players_except = players_future.exception()

    if isinstance(info_except, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="Server did not respond.", server=server_arg), 200
    elif isinstance(info_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response.", server=server_arg), 200
    elif info_except is not None:
        raise info_except

    info_res = info_future.result()

    if isinstance(players_except, socket.timeout):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server did not respond."), 200
    elif isinstance(players_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server sent a broken response."), 200
    elif players_except is not None:
        raise players_except

    players_res = players_future.result()

    return render_template("serverinfo.html", status="Success",
                           info=info_res, players=players_res), 200


@xiaocaoserverlist.route("/27160")
def xiaocao7():
    ip = '119.188.247.66'
    port = '27161'
    port = int(port)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        info_future = pool.submit(
            a2s.info, (ip, port), timeout=QUERY_TIMEOUT)
        players_future = pool.submit(
            a2s.players, (ip, port), timeout=QUERY_TIMEOUT)
    concurrent.futures.wait((info_future, players_future))

    info_except = info_future.exception()
    players_except = players_future.exception()

    if isinstance(info_except, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="Server did not respond.", server=server_arg), 200
    elif isinstance(info_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response.", server=server_arg), 200
    elif info_except is not None:
        raise info_except

    info_res = info_future.result()

    if isinstance(players_except, socket.timeout):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server did not respond."), 200
    elif isinstance(players_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server sent a broken response."), 200
    elif players_except is not None:
        raise players_except

    players_res = players_future.result()

    return render_template("serverinfo.html", status="Success",
                           info=info_res, players=players_res), 200


@xiaocaoserverlist.route("/27170")
def xiaocao8():
    ip = '119.188.247.66'
    port = '27171'
    port = int(port)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        info_future = pool.submit(
            a2s.info, (ip, port), timeout=QUERY_TIMEOUT)
        players_future = pool.submit(
            a2s.players, (ip, port), timeout=QUERY_TIMEOUT)
    concurrent.futures.wait((info_future, players_future))

    info_except = info_future.exception()
    players_except = players_future.exception()

    if isinstance(info_except, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="Server did not respond.", server=server_arg), 200
    elif isinstance(info_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response.", server=server_arg), 200
    elif info_except is not None:
        raise info_except

    info_res = info_future.result()

    if isinstance(players_except, socket.timeout):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server did not respond."), 200
    elif isinstance(players_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server sent a broken response."), 200
    elif players_except is not None:
        raise players_except

    players_res = players_future.result()

    return render_template("serverinfo.html", status="Success",
                           info=info_res, players=players_res), 200


@xiaocaoserverlist.route("/27180")
def xiaocao9():
    ip = '119.188.247.66'
    port = '27181'
    port = int(port)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        info_future = pool.submit(
            a2s.info, (ip, port), timeout=QUERY_TIMEOUT)
        players_future = pool.submit(
            a2s.players, (ip, port), timeout=QUERY_TIMEOUT)
    concurrent.futures.wait((info_future, players_future))

    info_except = info_future.exception()
    players_except = players_future.exception()

    if isinstance(info_except, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="Server did not respond.", server=server_arg), 200
    elif isinstance(info_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response.", server=server_arg), 200
    elif info_except is not None:
        raise info_except

    info_res = info_future.result()

    if isinstance(players_except, socket.timeout):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server did not respond."), 200
    elif isinstance(players_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server sent a broken response."), 200
    elif players_except is not None:
        raise players_except

    players_res = players_future.result()

    return render_template("serverinfo.html", status="Success",
                           info=info_res, players=players_res), 200


@xiaocaoserverlist.route("/27190")
def xiaocao10():
    ip = '119.188.247.66'
    port = '27191'
    port = int(port)

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        info_future = pool.submit(
            a2s.info, (ip, port), timeout=QUERY_TIMEOUT)
        players_future = pool.submit(
            a2s.players, (ip, port), timeout=QUERY_TIMEOUT)
    concurrent.futures.wait((info_future, players_future))

    info_except = info_future.exception()
    players_except = players_future.exception()

    if isinstance(info_except, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="Server did not respond.", server=server_arg), 200
    elif isinstance(info_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response.", server=server_arg), 200
    elif info_except is not None:
        raise info_except

    info_res = info_future.result()

    if isinstance(players_except, socket.timeout):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server did not respond."), 200
    elif isinstance(players_except, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="InfoOnly",
                               info=info_res, error="Server sent a broken response."), 200
    elif players_except is not None:
        raise players_except

    players_res = players_future.result()

    return render_template("serverinfo.html", status="Success",
                           info=info_res, players=players_res), 200
