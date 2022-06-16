from turtle import title
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'reservation'

mysql = MySQL(app)



@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM reservation")
    data = cur.fetchall()
    cur.close()



    #  return render_template('auth.html', students=data )
    return render_template('index2.html', reservation=data )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        title = request.form['title']
        start_event = request.form['start_event']
        end_event = request.form['end_event']
      
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO reservation (name, email, title, start_event,end_event) VALUES (%s, %s, %s, %s, %s)", (name, email, title,start_event,end_event))
        mysql.connection.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM reservation WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        title = request.form['title']
        start_event = request.form['start_event']
        end_event = request.form['end_event']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE reservation
               SET name=%s, email=%s, title=%s,start_event=%s, end_event=%s
               WHERE id=%s
            """, (name, email, title,start_event,end_event, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))









if __name__ == "__main__":
    app.run(debug=True)
