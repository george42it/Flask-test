from flask import Flask, render_template
# import flask 

app = Flask(__name__)

@app.route("/")
def base():
    return render_template("base.html")

@app.route("/test")
def test():
    return render_template("test.html")


if __name__ =="__main__":
    app.run(debug=False)