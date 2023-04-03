from cmath import log
from flask import render_template,request
from ..form import login
from ..models.action import Action
from ..models.info import Info
from ..models.quest import Quest
from ..models.menu import Menu
from ..models.menuInfo import MenuInfo
import datetime
import uuid
import random

def menu():
    group=random.choice(range(1,10))
    return render_template('menu.html',group=group)

def index():
    login_form=login.LoginForm()
    if request.method=="POST":
        tel=request.form['tel']
        ipAddr=request.headers['X-Forwarded-For']
        info=Info(userTel=tel)
        info.group=random.choice([9,3,11,7])
        info.ip=ipAddr
        info.save()
        return render_template('index.html',userTel=tel,group=info.group)
    return render_template('login.html',form=login_form)

def index2():
    login_form=login.LoginForm()
    if request.method=="POST":
        tel=request.form['tel']
        info=MenuInfo(userTel=tel)
        info.group=random.choice(range(1,10))
        info.save()
        return render_template('menu.html',group=info.group)
    return render_template('login2.html',form=login_form)

def test():
    return render_template('test.html',userTel=13811458985)

def welcome():
    return render_template('welcome.html')

def chess():
    return render_template('chess.html')

def study(group):
    return render_template('menu.html',group=group)

def learn(group):
    return render_template('index.html',group=group)

def api(col):
    if col=="quest":
        print(col)
        s=request.form
        q=Quest(**s)
        q.save()
        userUUID=Info.objects(userTel=s['userTel'])[0]['userUUID']
        return render_template('ends.html',code=str(userUUID)[-4:])
    elif col=="info":
        d=request.json
        if Info.objects(userTel=d['userTel']):
            userInfo=Info.objects(userTel=d['userTel'])[0]
            userInfo.userUUID=str(uuid.uuid4())
            userInfo.pixelRatio=d['pixelRatio']
            userInfo.screenWidth=d['screenWidth']
            userInfo.screenHeight=d['screenHeight']
            userInfo.save()


    elif col=="action":
        d=request.json
        action=Action(**d)
        print(action)
        action.save()
    elif col=='menu':
        d=request.json
        menu=Menu(**d)
        menu.save()
  
    return 'ok',200
    