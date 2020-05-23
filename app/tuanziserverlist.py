import concurrent.futures
import socket
import a2s
import jinja2

from flask import Blueprint, render_template

tuanziserverlist = Blueprint('tuanziserverlist', __name__, url_prefix='/tuanziserverlist')

QUERY_TIMEOUT = 3


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


@tuanziserverlist.route("/")
def tuanzilist():
    ip1 = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
    port1 = '27131'
    port1 = int(port1)

    ip2 = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
    port2 = '27132'
    port2 = int(port2)

    ip3 = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
    port3 = '27133'
    port3 = int(port3)

    ip4 = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
    port4 = '27139'
    port4 = int(port4)

    ip5 = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
    port5 = '27135'
    port5 = int(port5)

    ip6 = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
    port6 = '27136'
    port6 = int(port6)

    ip7 = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
    port7 = '27137'
    port7 = int(port7)

    ip8 = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
    port8 = '27134'
    port8 = int(port8)

    with concurrent.futures.ThreadPoolExecutor(max_workers=14) as pool:
        info_future1 = pool.submit(
            a2s.info, (ip1, port1), timeout=QUERY_TIMEOUT)
        info_future2 = pool.submit(
            a2s.info, (ip2, port2), timeout=QUERY_TIMEOUT)
        info_future3 = pool.submit(
            a2s.info, (ip3, port3), timeout=QUERY_TIMEOUT)
        info_future4 = pool.submit(
            a2s.info, (ip4, port4), timeout=QUERY_TIMEOUT)
        info_future5 = pool.submit(
            a2s.info, (ip5, port5), timeout=QUERY_TIMEOUT)
        info_future6 = pool.submit(
            a2s.info, (ip6, port6), timeout=QUERY_TIMEOUT)
        info_future7 = pool.submit(
            a2s.info, (ip7, port7), timeout=QUERY_TIMEOUT)
        info_future8 = pool.submit(
            a2s.info, (ip8, port8), timeout=QUERY_TIMEOUT)

    concurrent.futures.wait(
        (info_future1, info_future2, info_future3, info_future4, info_future5, info_future6, info_future7,
         info_future8))

    info_except1 = info_future1.exception()
    info_except2 = info_future2.exception()
    info_except3 = info_future3.exception()
    info_except4 = info_future4.exception()
    info_except5 = info_future5.exception()
    info_except6 = info_future6.exception()
    info_except7 = info_future7.exception()
    info_except8 = info_future8.exception()

    if isinstance(info_except1, socket.timeout):
        status1 = '离线'
        info_res1 = 'null'
    elif isinstance(info_except1, a2s.BrokenMessageError):
        status1 = '错误'
        info_res1 = 'null'
    elif info_except1 is None:
        info_res1 = info_future1.result()
        status1 = '在线'

    if isinstance(info_except2, socket.timeout):
        status2 = '离线'
        info_res2 = 'null'
    elif isinstance(info_except2, a2s.BrokenMessageError):
        status2 = '错误'
        info_res2 = 'null'
    elif info_except2 is None:
        info_res2 = info_future2.result()
        status2 = '在线'

    if isinstance(info_except3, socket.timeout):
        status3 = '离线'
        info_res3 = 'null'
    elif isinstance(info_except3, a2s.BrokenMessageError):
        status3 = '错误'
        info_res3 = 'null'
    elif info_except1 is None:
        info_res3 = info_future3.result()
        status3 = '在线'

    if isinstance(info_except4, socket.timeout):
        status4 = '离线'
        info_res4 = 'null'
    elif isinstance(info_except4, a2s.BrokenMessageError):
        status4 = '错误'
        info_res4 = 'null'
    elif info_except1 is None:
        info_res4 = info_future4.result()
        status4 = '在线'

    if isinstance(info_except5, socket.timeout):
        status5 = '离线'
        info_res5 = 'null'
    elif isinstance(info_except5, a2s.BrokenMessageError):
        status5 = '错误'
        info_res5 = 'null'
    elif info_except1 is None:
        info_res5 = info_future5.result()
        status5 = '在线'

    if isinstance(info_except6, socket.timeout):
        status6 = '离线'
        info_res6 = 'null'
    elif isinstance(info_except6, a2s.BrokenMessageError):
        status6 = '错误'
        info_res6 = 'null'
    elif info_except1 is None:
        info_res6 = info_future6.result()
        status6 = '在线'

    if isinstance(info_except7, socket.timeout):
        status7 = '离线'
        info_res7 = 'null'
    elif isinstance(info_except7, a2s.BrokenMessageError):
        status7 = '错误'
        info_res7 = 'null'
    elif info_except1 is None:
        info_res7 = info_future7.result()
        status7 = '在线'

    if isinstance(info_except8, socket.timeout):
        status8 = '离线'
        info_res8 = 'null'
    elif isinstance(info_except8, a2s.BrokenMessageError):
        status8 = '错误'
        info_res8 = 'null'
    elif info_except8 is None:
        status8 = '在线'
        info_res8 = info_future8.result()

    return render_template("tuanziserverlist.html", status="Success", info1=info_res1, info2=info_res2, info3=info_res3,
                           info4=info_res4, info5=info_res5, info6=info_res6, info7=info_res7, info8=info_res8,
                           Status1=status1,
                           Status2=status2, Status3=status3, Status4=status4, Status5=status5, Status6=status6,
                           Status7=status7,
                           Status8=status8), 200


@tuanziserverlist.route("/tuanzi1")
def tuanzi1():
    ip = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
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


@tuanziserverlist.route("/tuanzi2")
def tuanzi2():
    ip = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
    port = '27132'
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


@tuanziserverlist.route("/tuanzi3")
def tuanzi3():
    ip = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
    port = '27133'
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


@tuanziserverlist.route("/tuanzi4")
def tuanzi4():
    ip = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
    port = '27139'
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


@tuanziserverlist.route("/tuanzi5")
def tuanzi5():
    ip = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
    port = '27135'
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


@tuanziserverlist.route("/tuanzi6")
def tuanzi6():
    ip = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
    port = '27136'
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


@tuanziserverlist.route("/tuanzi7")
def tuanzi7():
    ip = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
    port = '27137'
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


@tuanziserverlist.route("/tuanzi8")
def tuanzi8():
    ip = 'ABE1AE906330544B9D3E3D2EE3EFD3605.asuscomm.com'
    port = '27134'
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
