from flask import Flask, render_template, request,redirect,url_for
import sqlite3
app = Flask(__name__)

app.config['SECRET_KEY'] = 'n9y934yiug14gi8g3g4ilg134'

data = [{
            'name':'Ayush Basak'
        },
        {
            'name':'Ayush Basak'
        },
        {
            'name':'Ayush Basak'
        },
        {
            'name':'Ayush Basak'
        },
        {
            'name':'Ayush Basak'
        }
]

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
    else:
        cursor.execute('select * from data')
        fetchedData = cursor.fetchall()
        type(fetchedData)
        li = []
        for i in range(1,len(fetchedData)):
            print(i)
            dictionary = {}
            dictionary['name'] = fetchedData[i][0]
            dictionary['post'] = fetchedData[i][1]
            li.append(dictionary)
        print(li)
        return render_template("index.html",dataset=li)
    con.commit()
    con.close()

if __name__ == '__main__':
    app.run(debug=True)