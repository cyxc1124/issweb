import concurrent.futures
import socket

import a2s
from flask import Flask, render_template, redirect

QUERY_TIMEOUT = 3

app = Flask(__name__)


@app.template_filter("yesno")
def yesno(value):
    if value:
        return "Yes"
    else:
        return "No"


@app.template_filter("server_type")
def server_type(value):
    return {
        "d": "Dedicated",
        "l": "Non-dedicated",
        "p": "SourceTv relay"
    }.get(value, value)


@app.template_filter("platform")
def platform(value):
    return {
        "l": "Linux",
        "w": "Windows",
        "m": "macOS"
    }.get(value, value)


@app.template_filter("duration")
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


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/joinus")
def joinus():
    return redirect('https://jq.qq.com/?_wv=1027&k=5XnZwfy')


@app.route("/serverlist")
def serverlist():
    ip1 = '119.188.247.66'
    port1 = '27101'
    port1 = int(port1)

    ip2 = '119.188.247.66'
    port2 = '27111'
    port2 = int(port2)

    ip3 = '119.188.247.66'
    port3 = '27121'
    port3 = int(port3)

    ip4 = '119.188.247.66'
    port4 = '27131'
    port4 = int(port4)

    ip5 = '119.188.247.66'
    port5 = '27141'
    port5 = int(port5)

    ip6 = '119.188.247.66'
    port6 = '27151'
    port6 = int(port6)

    ip7 = '119.188.247.66'
    port7 = '27161'
    port7 = int(port7)

    ip8 = '119.188.247.66'
    port8 = '27171'
    port8 = int(port8)

    ip9 = '119.188.247.66'
    port9 = '27181'
    port9 = int(port9)

    ip10 = '119.188.247.66'
    port10 = '27191'
    port10 = int(port10)

    ip11 = '119.188.247.66'
    port11 = '27201'
    port11 = int(port11)

    ip12 = '119.188.247.66'
    port12 = '27211'
    port12 = int(port12)

    ip13 = '119.188.247.66'
    port13 = '27221'
    port13 = int(port13)

    ip14 = '119.188.247.66'
    port14 = '27231'
    port14 = int(port14)

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
        info_future9 = pool.submit(
            a2s.info, (ip9, port9), timeout=QUERY_TIMEOUT)
        info_future10 = pool.submit(
            a2s.info, (ip10, port10), timeout=QUERY_TIMEOUT)
        info_future11 = pool.submit(
            a2s.info, (ip11, port11), timeout=QUERY_TIMEOUT)
        info_future12 = pool.submit(
            a2s.info, (ip12, port12), timeout=QUERY_TIMEOUT)
        info_future13 = pool.submit(
            a2s.info, (ip13, port13), timeout=QUERY_TIMEOUT)
        info_future14 = pool.submit(
            a2s.info, (ip14, port14), timeout=QUERY_TIMEOUT)

    concurrent.futures.wait(
        (info_future1, info_future2, info_future3, info_future4, info_future5, info_future6, info_future7,
         info_future8, info_future9, info_future10, info_future11, info_future12, info_future13, info_future14))

    info_except1 = info_future1.exception()
    info_except2 = info_future2.exception()
    info_except3 = info_future3.exception()
    info_except4 = info_future4.exception()
    info_except5 = info_future5.exception()
    info_except6 = info_future6.exception()
    info_except7 = info_future7.exception()
    info_except8 = info_future8.exception()
    info_except9 = info_future9.exception()
    info_except10 = info_future10.exception()
    info_except11 = info_future11.exception()
    info_except12 = info_future12.exception()
    info_except13 = info_future13.exception()
    info_except14 = info_future14.exception()

    if isinstance(info_except1, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="1服务器没有相应"), 200
    elif isinstance(info_except1, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response."), 200
    elif info_except1 is not None:
        raise info_except1

    if isinstance(info_except2, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="2服务器没有相应"), 200
    elif isinstance(info_except2, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response."), 200
    elif info_except2 is not None:
        raise info_except2

    if isinstance(info_except3, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="3服务器没有相应"), 200
    elif isinstance(info_except3, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response."), 200
    elif info_except3 is not None:
        raise info_except3

    if isinstance(info_except4, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="4服务器没有相应"), 200
    elif isinstance(info_except4, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response."), 200
    elif info_except4 is not None:
        raise info_except4

    if isinstance(info_except5, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="5服务器没有相应"), 200
    elif isinstance(info_except5, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response."), 200
    elif info_except5 is not None:
        raise info_except5

    if isinstance(info_except6, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="6服务器没有相应"), 200
    elif isinstance(info_except6, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response."), 200
    elif info_except6 is not None:
        raise info_except6

    if isinstance(info_except7, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="7服务器没有相应"), 200
    elif isinstance(info_except7, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response."), 200
    elif info_except7 is not None:
        raise info_except7

    if isinstance(info_except8, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="8服务器没有相应"), 200
    elif isinstance(info_except8, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response."), 200
    elif info_except8 is not None:
        raise info_except8

    if isinstance(info_except9, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="9服务器没有相应"), 200
    elif isinstance(info_except9, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response."), 200
    elif info_except9 is not None:
        raise info_except9

    if isinstance(info_except10, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="10服务器没有相应"), 200
    elif isinstance(info_except10, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response."), 200
    elif info_except10 is not None:
        raise info_except10

    if isinstance(info_except11, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="11服务器没有相应"), 200
    elif isinstance(info_except11, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response."), 200
    elif info_except11 is not None:
        raise info_except11

    if isinstance(info_except12, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="12服务器没有相应"), 200
    elif isinstance(info_except12, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response."), 200
    elif info_except12 is not None:
        raise info_except12

    if isinstance(info_except13, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="13服务器没有相应"), 200
    elif isinstance(info_except13, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response."), 200
    elif info_except13 is not None:
        raise info_except13

    if isinstance(info_except14, socket.timeout):
        return render_template("serverinfo.html", status="Error",
                               error="14服务器没有相应"), 200
    elif isinstance(info_except14, a2s.BrokenMessageError):
        return render_template("serverinfo.html", status="Error",
                               error="Server sent a broken response."), 200
    elif info_except14 is not None:
        raise info_except14

    info_res1 = info_future1.result()
    info_res2 = info_future2.result()
    info_res3 = info_future3.result()
    info_res4 = info_future4.result()
    info_res5 = info_future5.result()
    info_res6 = info_future6.result()
    info_res7 = info_future7.result()
    info_res8 = info_future8.result()
    info_res9 = info_future9.result()
    info_res10 = info_future10.result()
    info_res11 = info_future11.result()
    info_res12 = info_future12.result()
    info_res13 = info_future13.result()
    info_res14 = info_future14.result()

    # return render_template("serverlist.html")
    return render_template("serverlist.html", status="Success", info1=info_res1, info2=info_res2, info3=info_res3,
                           info4=info_res4, info5=info_res5, info6=info_res6, info7=info_res7, info8=info_res8,
                           info9=info_res9, info10=info_res10, info11=info_res11, info12=info_res12, info13=info_res13,
                           info14=info_res14), 200


@app.route("/serverlist/iss1")
def iss1():
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

@app.route("/serverlist/iss2")
def iss2():
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

@app.route("/serverlist/iss3")
def iss3():
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

@app.route("/serverlist/iss4")
def iss4():
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

@app.route("/serverlist/iss5")
def iss5():
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

@app.route("/serverlist/iss6")
def iss6():
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

@app.route("/serverlist/iss7")
def iss7():
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

@app.route("/serverlist/iss8")
def iss8():
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

@app.route("/serverlist/iss9")
def iss9():
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

@app.route("/serverlist/iss10")
def iss10():
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

@app.route("/serverlist/iss11")
def iss11():
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

@app.route("/serverlist/iss12")
def iss12():
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

@app.route("/serverlist/iss13")
def iss13():
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

@app.route("/serverlist/iss14")
def iss14():
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

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
