from flask import Flask, redirect, request

app = Flask(__name__, static_url_path="/static")

@app.route('/')

def index():

    page = ""

    return page

@app.route("/blog/hello")

def hr():

  return redirect("/hello")

@app.route("/blog/bye")

def br():

  return redirect("/bye")

@app.route('/hello', methods = ["GET"])

def hello():

    data = request.args

    template = "default"

    if data != {}:

      template = data["template"]

    title = "Hello World"

    date = "October 25th"

    text = "Here is my first blog entry."

    page = ""

    f = open("template/blog.html", "r")

    page = f.read()

    f.close()

    page = page.replace("{title}", title)

    page = page.replace("{date}", date)

    page = page.replace("{text}", text)

    page = page.replace("{template}", template)

  

    return page

@app.route('/bye', methods = ["GET"])

def bye():

    data = request.args

    template = "default"

    if data != {}:

      template = data["template"]

    title = "Bye World"

    date = "October 25th"

    text = "Here is my last blog entry."

    page = ""

    f = open("template/blog.html", "r")

    page = f.read()

    f.close()

    page = page.replace("{title}", title)

    page = page.replace("{date}", date)

    page = page.replace("{text}", text)

    page = page.replace("{template}", template)

  

    return page

  

app.run(host='0.0.0.0', port=81)

