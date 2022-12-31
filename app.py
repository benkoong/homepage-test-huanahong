from flask import Flask,render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField ,SubmitField
import os
SECRET_KEY = os.urandom(32)


app = Flask(__name__)

class MyForm(FlaskForm):
    name = StringField("ป้อนชื่อของคุณ")
    submit = SubmitField("บันทึก")

@app.route('/',methods=['GET','POST'])
def index():
    name = False
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
    return render_template("index.html", form = form, name= name)

@app.route('/about')
def about():
    #ส่งค่า แบบ Dictionary
    data = {"name":"laoamarin","age":30,"salary":"5,000"}
    products = ["เสื้อผ้า","เตารีด","ผ้าห่ม"]
    return render_template("about.html",mydata = data,myProducts = products)

@app.route('/admin')
def profile():
    #ชื่อ อายุ
    name = "benkoong"
    return render_template("admin.html",myname = name)

@app.route('/user/<name>/<age>')
def member(name,age):
    return "สวัสดีสมาชิก : ชื่อ {} , อายุ {} ".format(name[0],age)

@app.route('/sendData')
def signupForm():
    fname = request.args.get('fname')
    description = request.args.get('description')
    return  render_template("thankyou.html",data  = {"fname":fname,"description":description})


app.config['SECRET_KEY'] = SECRET_KEY

if __name__ == "__main__":
    app.run(debug=True)

