"""
 Aplikacja wykorzystujaca microframework Bottle
"""
from bottle import route, run, template, get, post, error, abort
from bottle import request, response
import requests
import datetime
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36'
}

"""
https://stooq.pl/q/d/l/?s=pkn&d1=20200101&d2=20200221&i=d
"""
def get_stock_data(ticker, start, stop):
    ticker = ticker.lower()
    start = start.replace("-","")
    stop = stop.replace("-","")
    url = f"https://stooq.pl/q/d/l/?s={ticker}&d1={start}&d2={stop}&i=d"
    data = {}
    try:
        r = requests.get(url, headers=headers)
        lines = r.text.split("\n")
        for index, line in enumerate(lines):
            if index==0 or line.strip()=="":
                continue
            try:
                day_, o_, h_, l_, c_, v_ = line.strip().split(",")
                data[day_] = (float(c_), int(v_))
            except:
                pass
        # zwroc dane wynikowe
        return data
    except Exception as exc:
        return None

@route("/getstock")
def getstock():
    ticker = request.query.ticker
    start = request.query.start
    stop = request.query.stop
    data = get_stock_data(ticker, start, stop)
    if data is None:
        abort(500, "Nie można pobrać danych")
    else:
        response.set_header("Content-type", "application/json")
        s = json.dumps(data)
        return s

@route("/getstockhtml")
def getstockhtml():
    ticker = 'cdr'
    start = "2020-01-01"
    stop = "2020-02-20"
    data = get_stock_data(ticker, start, stop)
    if data is None:
        abort(500, "Nie można pobrać danych")
    else:
        return template("stock", ticker=ticker.upper(), stockdata=data)

@route("/getstockplot")
def getstockplot():
    ticker = 'cdr'
    start = "2020-01-01"
    stop = "2020-02-20"
    data = get_stock_data(ticker, start, stop)
    if data is None:
        abort(500, "Nie można pobrać danych")
    else:
        dates_list, closes_list, volumes_list = [], [], []
        for key, value in data.items():
            dates_list.append(f"\"{key}\"")
            closes_list.append(str(value[0]))
            volumes_list.append(str(value[1]))
        return template("plot", ticker=ticker.upper(),
                       dates=",".join(dates_list),
                        closes=",".join(closes_list),
                        volumes=",".join(volumes_list))

@route("/")
def index():
    return "Hello world!"

@route("/currenttime")
def currenttime():
    return f"Current datetime : {datetime.datetime.now()}"

@route("/message/<name>", method=['GET','POST'])
def message(name):
    return f"Wprowadziłes: {name} "

@get("/login")
def login_form():
    return """
        <form method='POST' action='/login'>
        <input name='username' type='text'>
        <input name='password' type='password'>
        <input type='submit'>
    """
@post("/login")
def login_submit():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if username=="admin" and password=="admin2020":
        response.set_cookie("account", username)
        return "Zalogowany"
    else:
        return "Niepoprawne dane logowania"

@get("/islogged")
def islogged():
    return request.get_cookie("account")

@route("/counter")
def counter():
    count = int(request.cookies.get('counter', '0'))
    count += 1
    response.set_cookie("counter", str(count))
    return f"Twoja {count} wizyta na stronie"

@error(404)
def error404(error):
    return f"Nie znaleziono strony, sprawdz adres URL - {error}"

@route("/isweekend")
def is_weekend_func():
    is_weekend_flag = datetime.date.today().weekday() >= 5
    return template("test.html", is_weekend=is_weekend_flag )

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True, reloader=True)