from flask import Flask, request

app = Flask(__name__)

logins = {}

logins["Sandee"] = {"email": "sandeetee9@gmail.com", "password": "pass1"}

logins["Tee"] = {"email": "hackerhex@gmail.com", "password": "pass2"}

logins["Sandra"] = {"email": "coderzee1@gmail.com", "password": "pass3"}

  

@app.route('/')

def index():

  page = """

  <form method = "post" action="/login">

        <p>Name: <input type="text" name="username" required> </p>

        <p>Email: <input type="email" name="email" required></p>

        <p>Password: <input type="password" name="password" required></p>

        <button type="submit">Save Data</button>

    </form>

    """

  return page

@app.route("/login", methods=["POST"])

def login():

  form = request.form

  isThere = False

  details = {}

  try:

    details = logins[form["username"]]

    isThere = True

  except:

    return "Username, email or password incorrect"

  if form["email"] == details["email"] and form["password"] == details["password"]:

    return "You are logged in"

  else:

    return "Email or password incorrect"

  

if __name__ == '__main__':

    app.run(debug=True)

#app.run(host='0.0.0.0', port=81)

