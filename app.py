from flask import Flask, redirect, render_template,request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='python'

mysql=MySQL(app)


@app.route('/reg',methods=['GET','POST'])
def reg():
    if request.method=='POST':
        fm=request.form

        a=fm['name']
        b=fm['email']
        c=fm['password']
        d=fm['mobile']

        q="insert into member(name,email,password,mobile) values ('"+a+"','"+b+"','"+c+"','"+d+"')"

        cursor=mysql.connection.cursor()
        cursor.execute(q)
        mysql.connection.commit()
        return redirect('/index')


    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/index')
def index():
    cursor=mysql.connection.cursor()
    q="select * from durgesh"
    cursor.execute(q)
    res=cursor.fetchall()
    return render_template('index.html',users=res)

@app.route('/')
def home():
    return render_template('home.html')

# @app.route('/book')
# def book():
#     return render_template('book.html')

@app.route('/ticket',methods=['GET','POST'])
def ticket():
    return render_template('ticket.html')
    

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/users')
def user():
    cursor=mysql.connection.cursor()
    q="select * from emp"
    cursor.execute(q)
    res=cursor.fetchall()


    return render_template('users.html',users=res)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/delete/<string:id>')
def delete(id):
    q="delete from emp where id='"+id+"'"
    cursor=mysql.connection.cursor()
    cursor.execute(q)
    mysql.connection.commit()
    return redirect('/users')

@app.route('/book/<string:id>')
def book(id):
    cursor=mysql.connection.cursor()
    q="select * from durgesh where id='"+id+"'"
    cursor.execute(q)
    res=cursor.fetchall()
    return render_template('book.html',users=res)


@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        fm=request.form

        a=fm['name']
        b=fm['salary']
        c=fm['email']
        d=fm['id']

        q="update emp set name='"+a+"',salary='"+b+"',email='"+c+"' where id='"+d+"'"

        cursor=mysql.connection.cursor()
        cursor.execute(q)
        mysql.connection.commit()
        return redirect('/index')

@app.route('/search',methods=['GET','POST'])
def search():
    if request.method=='POST':
        fm=request.form
        a=fm['search']

        q="select * from emp where name='"+a+"'"
        cursor=mysql.connection.cursor()
        cursor.execute(q)
        res=cursor.fetchall()
        return render_template('users.html',users=res)

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/create',methods=['GET','POST'])
def create():
    if request.method=='POST':
        fm=request.form
        a=fm['seat']
        b=fm['payment']
        c=fm['id']
        q="insert into ticket(match_id,seat,payment) values ('"+str(c)+"','"+str(a)+"','"+str(b)+"')"
        cursor=mysql.connection.cursor()
        cursor.execute(q)
        mysql.connection.commit()
        return redirect('/fetch')



@app.route('/fetch')
def fetch():
    cursor=mysql.connection.cursor()
    q="select * from ticket"
    cursor.execute(q)
    res=cursor.fetchall()
    q1="select * from durgesh"
    cursor.execute(q1)
    res1=cursor.fetchall()
    return render_template('ticket.html',users=res)

# @app.route('/fetch/<string:id>')
# def test(id):  
#     cursor=mysql.connection.cursor()
#     q="select * from ticket where match_id='"+id+"'"
#     cursor.execute(q)
#     res=cursor.fetchall() 
#     return render_template('ticket.html',users=res)




app.run(debug=True)