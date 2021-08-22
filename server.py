from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "b'\xb6\xffE\\\x9eg5*nL\xaf\xf8j*q"


@app.route('/')
def index():
    session['visits'] = session['visits'] + 1
    return render_template("index.html")


@app.route('/count', methods=['POST'])
def count():
    return redirect('/')


@app.route('/clear', methods=['POST'])
def clear():
    session['visits'] = 0

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
