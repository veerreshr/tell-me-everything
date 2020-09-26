from flask import Flask, render_template, request,redirect,url_for
import sqlite3
app = Flask(__name__)

app.config['SECRET_KEY'] = 'n9y934yiug14gi8g3g4ilg134'

@app.route('/',methods = ['GET','POST'])
@app.route('/home')
def home():
    con = sqlite3.connect('database.db')
    cursor = con.cursor()
    if(request.method == 'POST'):
        username = request.form['username']
        post = request.form['post']
        if(username == 'admin' and post == 'deletealldata'):
            cursor.execute('delete from data')
        else:
            cursor.execute('insert into data(name,post) values(?,?)',(username,post))
        con.commit()
        return redirect(url_for('home'))
    elif(request.method == 'GET'):
        cursor.execute('select * from data')
        fetchedData = cursor.fetchall()
        type(fetchedData)
        li = []
        for i in range(0,len(fetchedData)):
            print(i)
            dictionary = {}
            dictionary['name'] = fetchedData[i][0]
            dictionary['post'] = fetchedData[i][1]
            li.append(dictionary)
        return render_template("index-about.html",dataset=li,maxlength = 240)
    else:
        pass
    con.commit()
    con.close()

@app.route('/about')
def about():
    return render_template('about-min.html')

if __name__ == '__main__':
    app.run(host = "0.0.0.0",debug=False)