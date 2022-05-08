from django.shortcuts import render, redirect
import pymongo
import random

url = "mongodb+srv://aungkaungkhant:AungKaungKhant@cluster0.tmba9.mongodb.net/mini-banking-system?retryWrites=true&w=majority"
connection = pymongo.MongoClient(url)
database = connection["mini-banking-system"]
collection = database["User Info"]

storage = {}

def get():
    for i in collection.find():
        _id = i['_id']
        username = i['username']
        passcode = i['passcode']
        amount = i['amount']
        data = {_id: {'id': _id, 'username':username, 'passcode':passcode, 'amount':amount}}
        storage.update(data)

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'signup.html')

def exist(username):
    get()
    for i in storage:
        if username == storage.get(i)['username']:
            return True

    return False

def register(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        amount = request.POST['amount']
        flag = exist(username)

        if not flag:
            randomNum = random.randint(000000,999999)
            info = {"_id":randomNum, "username":username, "passcode":password, "amount":amount}
            collection.insert_one(info)
            get()
            return render(request, 'data.html', {'data': storage})

        else:
            return render(request, 'signup.html', {'alert': 'Username already exists.', 'username': username})

    except:
        return render(request, 'signup.html', {'alert': 'Please fill the form.'})

def signin(request):
    return render(request, 'signin.html')

def check(username, passcode):
    get()
    for i in storage:
        if username == storage.get(i)['username'] and passcode == storage.get(i)['passcode']:
            return True

    return False

def login(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        flag = check(username, password)

        if flag:
            get()
            return render(request, 'data.html', {'data': storage})

        else:
            return render(request, 'signin.html', {'alert': 'Incorrect Username or Password', 'username': username})

    except:
        return render(request, 'signin.html', {'alert': 'Please fill the form.'})