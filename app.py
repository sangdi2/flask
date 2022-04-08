from flask import Flask,render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/movie')
def movie():  # put application's code here
    con =sqlite3.connect("movie.db")
    cur =con.cursor()
    sql="select * from movie"
    execute=cur.execute(sql)
    data=[]
    for item in execute:
        data.append(item)
    cur.close()
    con.close()
    return render_template("movie.html",movies=data)

@app.route('/score')
def score():  # put application's code here
    con = sqlite3.connect("movie.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie group by score"
    execute = cur.execute(sql)
    score=[]
    num=[]
    for item in execute:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    con.close()

    return render_template("score.html",score=score,num=num)

@app.route('/ciyun')
def ciyun():  # put application's code here
    return render_template("ciyun.html")

@app.route('/team')
def team():  # put application's code here
    return render_template("team.html")


if __name__ == '__main__':
    app.run()
