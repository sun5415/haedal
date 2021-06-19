#라이브러리 = 개발 활용가능한 도구의 집합
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return '2018115415 경상대학 경제통상학부 권순성'

@app.route('/me/')
def my():
    return render_template('index.html', car.jpg)

if __name__ == "__main__":
    app.run(debug = True)

