from flask import Flask, render_template, request, redirect, url_for
from todo import Mind

app = Flask(__name__)

try:
    mind = Mind.load()
except:
    mind = Mind(tasks=[])


@app.route("/add", methods=["POST"])
def add_task():
    newtask = request.form.get("newtask")
    if not newtask:
        return redirect(url_for("mind_web_interface"))
    mind.add_task(newtask)
    return redirect(url_for("mind_web_interface"))


@app.route("/")
def mind_web_interface():
    return render_template("todolist.html", tasks=mind.tasks)
