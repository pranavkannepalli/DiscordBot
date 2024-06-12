import pyrebase

firebase_config:dict[str, str] = {
    "apiKey": "AIzaSyBBoP5nb1cbHCENcOsV9mYNEyCPg4Ed6Kw",
    "authDomain": "todo-list-aa205.firebaseapp.com",
    "databaseURL": "https://todo-list-aa205-default-rtdb.firebaseio.com",
    "projectId": "todo-list-aa205",
    "storageBucket": "todo-list-aa205.appspot.com",
    "messagingSenderId": "210858993508",
    "appId": "1:210858993508:web:8cd175132dd27f3941fc71",
    "measurementId": "G-SEB45ZG4FF"
}

firebase = pyrebase.initialize_app(firebase_config)

db = firebase.database()

print(db.child("N3BgYDG1Bpfk1aqeiMp6BBqbFw13").child("Tasks").get())

def get_response(inp: str) -> str:
    return "Hello there"