import psycopg2
from flask import *

app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def main():
    post = {}
    if request.method == "POST":
        conn = psycopg2.connect(database="test", user="postgres", password="p0576r35", host="localhost")
        input = request.form["text"]
        query = "select nom from personnes where id="+str(input).replace(" or ", "")
        cur = conn.cursor()
        cur.execute(query)
        out = []
        for row in cur:
            out.append(row)
        post['name'] = out
    return render_template("index.html", posts=post)

"""@app.route("/page2")
def page2():
    return render_template("page2.html")"""

if __name__ == "__main__" :
    app.run()