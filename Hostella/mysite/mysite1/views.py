from django.shortcuts import render
from django.http import HttpResponse
import pyrebase


config ={
    'apiKey': "AIzaSyDpeG5G2AK8YGpJqFsqnZ1FOCDsjNN7Z44",
    'authDomain': "hostella-442cf.firebaseapp.com",
    'databaseURL': "https://hostella-442cf-default-rtdb.firebaseio.com",
    'projectId': "hostella-442cf",
    'storageBucket': "hostella-442cf.appspot.com",
    'messagingSenderId': "381429936975",
    'appId': "1:381429936975:web:e6ba1a0a772b69c2238b3a",
    'measurementId': "G-1QTRR5F7LF"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database = firebase.database()
storage = firebase.storage()

# Create your views here.
def index(request):
    firstname = database.child('user').child('fullname').child('firstname').get().val()
    lastname = database.child('user').child('fullname').child('lastname').get().val()
    fullname = firstname + ' ' + lastname
    return render(request, 'index.html',{
        'firstname':firstname,
        'lastname':lastname,
        'fullname':fullname
        })

def signIn(request):
    return render(request, 'signIn.html')