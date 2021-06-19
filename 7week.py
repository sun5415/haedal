from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/lunch/")
def lunch():
    return render_template('index.html', food_img=car.jpg)

if __name__ == "__main__":
    app.run(debug=True)
