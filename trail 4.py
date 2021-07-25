import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyBlB2OBLZU3ku6-CjGZmdsNY_ujSw5aC-U",
    "authDomain": "noted-flash-306012.firebaseapp.com",
    "databaseURL": "https://noted-flash-306012-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "noted-flash-306012",
    "storageBucket": "noted-flash-306012.appspot.com",
    "messagingSenderId": "822280810171",
    "appId": "1:822280810171:web:23bb2f142d57126afa039e"
}
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

data = {"my family":"I20CS", "my friends":"JDF50","lol":"ADF40"}


def send():
    db.child('rooms').child("I20CS").child("messages").push("second msg in I20CS")

def addgroup():
    d = db.child('user_details').child('ikamalesh_').child('rooms').get().val()
    d = dict(d)
    d['sample1'] = "DFS88"
    db.child('user_details').child('ikamalesh_').child('rooms').set(d)


db.child('rooms').child('99999').child('title')