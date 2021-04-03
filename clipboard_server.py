from flask import Flask
import psycopg2
import json
from flask_cors import cross_origin

con = psycopg2.connect(database="clipboard", user="aravind", password="", host="localhost", port="5432")

cur = con.cursor()

app = Flask(__name__)


@app.route('/')
@cross_origin()
def hello():
    cur.execute("SELECT * FROM public.clipboard_data")
    content_list = cur.fetchall()
    print(cur.rowcount)
    return json.dumps(content_list)


if __name__ == '__main__':
    app.run()

