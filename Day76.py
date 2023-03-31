from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def index():
    page= """
    <html>
    <body>
        <h2>Welcome. I'm Sandee. See:</h2>
        <ul>
            <li><a href= "/portfolio">Portfolio</a></li>
            <li><a href= "/resume">Resume</a></li>
        </ul>
    </body>
    </html>
    """
    return page


@app.route('/portfolio')
def portfolio():
    return redirect("https://sandee-portfolio-01.vercel.app/")
  
@app.route('/resume')
def resume():
    return redirect("https://drive.google.com/file/d/1lTzcYASpveT80PL2ZGCulvJIfTg0zy4Z/view?usp=drivesdk")

app.run(host='0.0.0.0', port=81)
