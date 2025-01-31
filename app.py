from flask import Flask,redirect,url_for,render_template,request
from sesametest import openSesame

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        openSesame()
        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=8000,debug=True)
