from flask import Flask

app = Flask(__name__)

myReflections = {}

myReflections["76"] = {"link" : "https://github.com/Sandee004/100-days-of-Python/blob/main/Day76/Day76.py", "Reflection" : "With the help of Flask, my web server is looking dope Day 76 of #Replit100DaysOfCode. Was a bit of a head scratcher, but I got there in the end. Even if I was a bit lazy with the css 😭"}

myReflections["77"] = {"link" : "https://github.com/Sandee004/100-days-of-Python/blob/main/Day77/Day77.py", "Reflection" : "Oh. Easy. Done. Boom. I can seriously create some legit web servers now thanks to Flask on Day 77 of #Replit100DaysOfCode"}

@app.route('/')

def home():

    return ("See <a href='https://day78100days.sandee004.repl.co/76'>here</a> or <a href='https://day78100days.sandee004.repl.co/77'>here</a>.")

@app.route('/<pageNumber>')

def index(pageNumber):

  global Reflections

  page = ""

  f = open("template/reflection.html", "r")

  page = f.read()

  f.close()

  

  page = page.replace("{day}", pageNumber)

  page = page.replace("{date}", myReflections[pageNumber]["link"])

  page = page.replace("{reflection}", myReflections[pageNumber]["Reflection"])

  return page

app.run(host='0.0.0.0', port=81)

