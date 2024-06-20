from flask import Flask,render_template
import requests
import json
app = Flask(__name__)

@app.route("/")
def homepage():
    url = "https://api.npoint.io/3c3fac46955db62d7e91"
    response = requests.get(url=url)
    data = response.json()
    with open('data.json') as f:
        d = json.load(f)
    return render_template("index.html" , data=d)


@app.route("/about")
def get_about():
    return render_template('about.html')


@app.route("/contact")
def get_contact():
    return render_template("contact.html")


@app.route("/post/<int:num>")
def get_post(num):
    url = "https://api.npoint.io/3c3fac46955db62d7e91"
    response = requests.get(url=url)
    data = response.json()

    with open('data.json') as f:
        d = json.load(f)
    return render_template('post.html', data=d , num=num)


if __name__ == "__main__":
    app.run(debug=True)

