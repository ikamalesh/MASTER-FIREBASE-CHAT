import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyBlB2OBLZU3ku6-CjGZmdsNY_ujSw5aC-U",
    'authDomain': "noted-flash-306012.firebaseapp.com",
    'databaseURL': "https://noted-flash-306012-default-rtdb.asia-southeast1.firebasedatabase.app",
    'projectId': "noted-flash-306012",
    'storageBucket': "noted-flash-306012.appspot.com",
    'messagingSenderId': "822280810171",
    'appId': "1:822280810171:web:23bb2f142d57126afa039e"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()


def new_user():
    username = input('Username > ')
    email = input('Email > ').replace('.','<dot>')
    password = input("Password > ")

    data = {
        "username": username,
        "email": email,
        "password": password
    }

    db.child('user_details').child(username).set(data)
    db.child('user_details').child('map').set({email: username})

def login():
    username = input('Username > ')
    password = input('Password > ')

    all = db.child('user_details').child(username).get().val()
    if password == all['password']:
        print('OK')
login()