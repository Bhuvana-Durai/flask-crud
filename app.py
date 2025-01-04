from flask import Flask,render_template,url_for,request,redirect
from flask_mysqldb import MySQL
app = Flask(__name__)

#for database connection
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Bhuvana@1"
app.config['MYSQL_DB'] = 'crud'
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
mysql = MySQL(app)


#homepage loading
@app.route("/")
def home():
    con = mysql.connection.cursor()
    sql = "select * from users"
    con.execute(sql)
    res = con.fetchall()
    return render_template("home.html",datas = res)

#user update
@app.route("/addusers",methods=['GET','POST'])
def addusers():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        con = mysql.connection.cursor()
        sql = "insert into users(NAME,AGE,CITY) values (%s,%s,%s)"
        con.execute(sql,[name,age,city])
        mysql.connection.commit()
        con.close()
        return redirect(url_for("home"))
    return render_template("addusers.html")



if(__name__ == '__main__'):
    app.run(debug=True)