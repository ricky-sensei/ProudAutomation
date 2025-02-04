from flask import Flask,redirect,url_for,render_template,request
from sesame_control import sesame_control
from time import sleep

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        response = sesame_control("open")
        disabled = "" 
        if response == "<Response [200]>":
            sleep(3)
            status = sesame_control("check_status")
            if status == "unlocked":
                result = "解錠成功 "+ response
                disabled = "disabled"
            else:
                result = "通信に成功しましたが、解錠に失敗しました"
        else:
            result = "通信に失敗しました"+ response
        return render_template('index.html', result=result, disabled=disabled)
    return render_template('index.html')

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=8000,debug=True)
