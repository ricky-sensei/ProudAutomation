from flask import Flask,redirect,url_for,render_template,request
from sesametest import openSesame

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        response = openSesame()
        disabled = "" 
        if response == "<Response [200]>":
            result = "解錠成功 "+ response
            disabled = "disabled"
        else:
            result = "解錠失敗？ "+ response
        return render_template('index.html', result=result, disabled=disabled)
    return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=8000,debug=True)
