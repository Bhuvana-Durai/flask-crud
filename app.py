from flask import Flask,render_template
from flask_mysqldb import MySQL
app = Flask(__name__)

#for database connection
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Bhuvana@1"
app.config['MYSQL_DB'] = 'crud'
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)


#creation of data
@app.route("/")
def home():
    con = mysql.connection.cursor()
    sql = "select * from users"
    con.execute(sql)
    res = con.fetchall()
    return render_template("home.html",datas = res)
if(__name__ == '__main__'):
    app.run(debug=True)