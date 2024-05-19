import handle_requests
from flask import Flask, redirect, render_template, url_for, request


app = Flask(__name__)
db = handle_requests.db()
user = None

@app.route('/', methods=["POST","GET"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        global user
        user = db.get_login(username, password)
        if user != []:
            print(user)
            if user[0]["account_type"] == "Consumer":
                return redirect("/consumer")
        return render_template("index.html", user=user)
    return render_template("index.html", user=None)

@app.route('/consumer')
def consumer():
    data = db.get_products()
    print(data)
    return render_template("consumer.html", data=str(data))

app.run(debug=True)



