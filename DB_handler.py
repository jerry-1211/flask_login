import pyrebase
import json

class DBModule : 
    def __init__(self):
        with open("./auth/firebaseAuth.json") as f :
            config = json.load(f)
        
        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def login(self,uid,pw):
        pass

    def singin(self,_id_,pwd,name):
        informations = {
            "uname" : name,
            "pwd" : pwd,
        }
        
        if self.sigin_verification(_id_):
            self.db.child("users").child(_id_).set(informations)
            return True
        else :
            return False

    def sigin_verification(self,uid):
        users = self.db.child("users").get().val()
        for i in users:
            if uid == i :
                return False
        return True

  