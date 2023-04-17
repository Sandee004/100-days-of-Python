from flask import Flask, request

app = Flask(__name__)

access= {"no": "no", "infinity": "infinity", "food": "Human food"}

@app.route('/')

def index():

  page = """

  <form method="post" action="/welcome">

  <p>Are you made of metal? <input type="radio" name="metal" value="yes">Yes <input type="radio" name="metal" value="no">No</p>

  <p>What is infinity + 1? <input type="text" name="infinity"></p>

  <p>

      Which is your favourite food

      <select name="food">

        <option>Nuts</option>

        <option>Human food</option>

        <option>Holographic chips</option>

      </select>

    </p>

    <button type="submit">I am not a robot</button>

  </form>

  """

  return page

@app.route("/welcome", methods=["POST"])

def welcome():

    page= ""

    form= request.form

    if form["metal"] == "no" and form["infinity"].lower().trim() == "infinity" and form["food"] == "Human food":

        page += "Welcome fellow human"

    else:

       page += "Robot detected. I see you"

    return page

    

    

if __name__ == '__main__':

    app.run(debug=True)

#app.run(host='0.0.0.0', port=81)
