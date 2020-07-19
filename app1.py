from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres993@localhost/tennis_goat'
db=SQLAlchemy(app)


class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(100), unique=True)
    goat_=db.Column(db.String)

    def __init__(self, email_, goat_):
        self.email_=email_
        self.goat_=goat_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form['email_name']
        response=request.form['goat']
        if db.session.query(Data).filter(Data.email_==email).count() == 0:
            data=Data(email, response)
            db.session.add(data)
            db.session.commit()
            count_total = db.session.query(Data.goat_).count()
            count_goat=db.session.query(Data).filter(Data.goat_==response).count()
            percentage_goat=round((count_goat/count_total)*100)
            send_email(email, response, percentage_goat, count_total)            
            return render_template("success.html")
    return render_template("index.html", text="Seems like we have a response from this email earlier!")

if __name__ == "__main__":
    app.debug=True
    app.run()