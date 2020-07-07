import concurrent.futures
import socket
import a2s
import jinja2

from flask import Blueprint, render_template

otherserverlist = Blueprint('otherserverlist', __name__, url_prefix='/otherserverlist')

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


@otherserverlist.route("/")
def otherlist():
    ip0 = '134.175.62.172'
    port0 = '27131'
    port0 = int(port0)

    try:
        server0_info = a2s.info((ip0, port0), timeout=0.1)
    except socket.timeout as e:
        server0_info = 'null'
    except a2s.BrokenMessageError as e:
        server0_info = 'null'
    else:
        pass

    ip = ['119.188.247.66', '119.188.247.66', '119.188.247.66', '119.188.247.66', '119.188.247.66', '119.188.247.66',
          '119.188.247.66', '119.188.247.66', '119.188.247.66', '119.188.247.66', '119.188.247.66', '119.188.247.66',
          '119.188.247.66', '119.188.247.66']
    port = ['27201', '27211', '27221', '27231', '27251', '27261', '27271', '27281', '27291', '27301', '27311',
            '27321', '27331', '27341']

    servers_info = []
    for (info_ip, info_port) in zip(ip, port):
        info_port = int(info_port)
        try:
            server_info = a2s.info((info_ip, info_port), timeout=0.2)
        except socket.timeout as e:
            server_info = 'null'
        except a2s.BrokenMessageError as e:
            server_info = 'null'
        else:
            pass
        servers_info.append(server_info)
    return render_template("otherserverlist.html", infos=servers_info, info0=server0_info), 200



@otherserverlist.route("/xiaolu")
def xiaolu():
    ip = '134.175.62.172'
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

@otherserverlist.route("/27200")
def other1():
    ip = '119.188.247.66'
    port = '27201'
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


@otherserverlist.route("/27210")
def other2():
    ip = '119.188.247.66'
    port = '27211'
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


@otherserverlist.route("/27220")
def other3():
    ip = '119.188.247.66'
    port = '27221'
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


@otherserverlist.route("/27230")
def other4():
    ip = '119.188.247.66'
    port = '27231'
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


@otherserverlist.route("/27240")
def other5():
    ip = '119.188.247.66'
    port = '27241'
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


@otherserverlist.route("/27250")
def other6():
    ip = '119.188.247.66'
    port = '27251'
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


@otherserverlist.route("/27260")
def other7():
    ip = '119.188.247.66'
    port = '27261'
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

@otherserverlist.route("/27200")
def other8():
    ip = '119.188.247.66'
    port = '27271'
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

@otherserverlist.route("/27280")
def other9():
    ip = '119.188.247.66'
    port = '27281'
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

@otherserverlist.route("/27290")
def other10():
    ip = '119.188.247.66'
    port = '27291'
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
                           
@otherserverlist.route("/27300")
def other11():
    ip = '119.188.247.66'
    port = '27301'
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

@otherserverlist.route("/27310")
def other12():
    ip = '119.188.247.66'
    port = '27311'
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


@otherserverlist.route("/27320")
def other13():
    ip = '119.188.247.66'
    port = '27321'
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


@otherserverlist.route("/27330")
def other14():
    ip = '119.188.247.66'
    port = '27331'
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
                           
@otherserverlist.route("/27340")
def other15():
    ip = '119.188.247.66'
    port = '27341'
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