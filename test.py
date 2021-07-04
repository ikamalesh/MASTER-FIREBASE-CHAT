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
