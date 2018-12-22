from flask import Flask,render_template,request
from send_mail_3 import SendMail
import sys
import datetime

app = Flask(__name__,template_folder='template')

@app.route("/",methods = ['GET','POST'])
def index():
    return render_template("index.html")

@app.route("/send_mail",methods = ['GET','POST'])
def add():
    f_name = request.form.get('first_name')
    l_name = request.form.get('last_name')
    mail = request.form.get('email')
    try:    
        result = SendMail().sendnail_3(mail)
        return result
    except:
        return "send mail error"

if __name__ == "__main__":
    app.run(debug=True)