from typing import OrderedDict
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

# Initial Auth
def authwithtoken_response(server:str, channel: str, token: str) -> str:
    try :
        db.child('discord_tokens').child(server).child(channel).set(token)
        return f"The given token is now associated with the channel: {token}"
    except Exception as e:
        return "Failed"
    
def todoToString(todo) -> str:
    todoString: str = str(todo["id"]) + ") " + todo["description"] + ", Added By: " + todo["addedBy"]
    if("date" in todo.keys()):
        todoString += ", Date: " + str(todo["date"])
    if("tag" in todo.keys() and todo["tag"] != "Untagged"):
        todoString += ", Tag: " + str(todo["tag"])
    todoString += "\n"

    if("Subtasks" in todo.keys()):
        for subtask in todo["Subtasks"].values():
            todoString += "|--> " + todoToString(subtask)

    return todoString

# Get Todos
def todosString(todos: OrderedDict) -> str:
    outputString = f""
    for todo in todos.values():
        if todo != None and not todo["isDone"]:
            todoString = todoToString(todo)
            outputString += todoString

    return outputString


def gettodos_response(server:str, channel:str) -> str:
    try:
        group = db.child('discord_tokens').child(server).child(channel).get().val()
        if(group):
            todos = db.child(group).child("Tasks").get().val()
            if(todos):
                return todosString(todos)
            else:
                return "The group that you are requesting for doesn't exist, has no todos, or is corrupted."
        else:
            return "You haven't authenticated for this app yet. Use /authwithtoken and supply a valid group name"
    except Exception as e:
        print(e)
        return "Huh, that's weird. Try again later when we fix this bug."
    
# Edit Todos

# Add Todos
def add_todo(server: str, channel: str, user:str, description: str):
    try:
        group = db.child('discord_tokens').child(server).child(channel).get().val()
        if(group):
            numTodos:int = db.child(group).child("LastId").get().val()
            print(numTodos)
            db.child(group).child("Tasks").child(numTodos + 1).set({"addedBy": user, "description": description, "id": numTodos + 1, "isDone": False, "Subtasks": []})
            db.child(group).child("LastId").set(numTodos + 1)
            return f"Successfully added your todo. Id is {numTodos + 1}"
        else:
            return "You haven't authenticated for this app yet. Use /authwithtoken and supply a valid group name"
    except Exception as e:
        print(e)
        return "Huh, that's weird. Either the todo doesn't exist or we're doing something wrong."

# Remove Todos
def remove_todo(server: str, channel: str, id: int) -> str:
    try:
        group = db.child('discord_tokens').child(server).child(channel).get().val()
        if(group):
            db.child(group).child("Tasks").child(id).remove()
            return f"Removed todo with id {id}"
        else:
            return "You haven't authenticated for this app yet. Use /authwithtoken and supply a valid group name"
    except Exception as e:
        print(e)
        return "Huh, that's weird. Either the todo doesn't exist or we're doing something wrong."
    
# Num Todos
def numtodos_response(server: str, channel: str) -> str:
    try:
        group = db.child('discord_tokens').child(server).child(channel).get().val()
        if(group):
            numTodos:int = db.child(group).child("LastId").get().val()
            print(numTodos)
            return f"{numTodos} have been created in this group."
        else:
            return "You haven't authenticated for this app yet. Use /authwithtoken and supply a valid group name"
    except Exception as e:
        print(e)
        return "Huh, that's weird. Either the todo doesn't exist or we're doing something wrong."