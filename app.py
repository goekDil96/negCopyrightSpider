from datetime import datetime
import os
import json

import random
from flask import Flask, render_template, request, render_template_string
import psycopg2
import pandas as pd

from dotenv import load_dotenv

load_dotenv(os.path.join(os.getcwd(), "config", ".env"))  # take environment variables from config/.env.

hostname = str(os.getenv("HOSTNAME"))
username = str(os.getenv("USER"))
password = str(os.getenv("PASSWORD"))
database = str(os.getenv("DATABASE"))
tablename = str(os.getenv("TABLENAME"))


app = Flask(__name__)
app.config["DEBUG"] = True


connection = psycopg2.connect(
    host=hostname, user=username, password=password,  
    dbname=database)
connection.set_client_encoding('UTF8')
cur = connection.cursor()

@app.route("/")
def index():
    return render_template_string("""<a href="/crawledExamples/">Get to database</a></br><a href="/evaluate_string">Evaluate strings</a>""")

@app.route('/crawledExamples/', defaults={'n' : None})
@app.route("/crawledExamples/<n>")
def hello_world(n):
    query = f"SELECT * FROM {tablename};"
    cur.execute(query)
    connection.commit()
    list_tables = cur.fetchall()
    df = pd.DataFrame(list_tables, columns = ['copyright_string', 'source', 'datetime', 'is_no_copyright_statement'])
    if n:
        df = df.to_html(max_rows=int(n))
    else:
        df = df.to_html()
    return df


@app.route("/evaluate_string", methods=["GET", "POST"])
def do_evaluation_of_string():
    query = f"SELECT * FROM {tablename} WHERE is_no_copyright_statement IS NULL;"
    cur.execute(query)
    connection.commit()
    list_tables = cur.fetchall()
    random_int = random.randint(0, len(list_tables)-1)
    df = pd.DataFrame(list_tables, columns = ['copyright_string', 'source', 'datetime', 'is_no_copyright_statement'])
    df = json.loads(df.iloc[random_int].to_json())
    copyright_string = df["copyright_string"]
    source = df["source"]

    if request.method == "POST":
        no_copyright = request.form.get("no_copyright")
        query = f"""UPDATE {tablename} SET is_no_copyright_statement = '{no_copyright}' WHERE (copyright_string = '{copyright_string}');"""
        cur.execute(query)
        connection.commit()

    return render_template("do_evaluation_of_string.html", copyright_string=copyright_string, source=source)
    

if __name__ == '__main__':
    app.run()


    