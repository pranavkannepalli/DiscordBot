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

def authwithtoken_response(server:str, channel: str, token: str) -> str:
    try :
        db.child('discord_tokens').child(server).child(channel).set(token)
        return f"The given token is now associated with the channel: {token}"
    except Exception as e:
        return "Failed"
    
def gettodos_response(server:str, channel:str) -> str:
    try:
        group = db.child('discord_tokens').child(server).child(channel).get().val()
        print(group)
        if(group):
            return "Succeeded"
        return "Failed"
    except Exception as e:
        return "Failed"