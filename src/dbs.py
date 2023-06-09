import firebase_admin
from firebase_admin import credentials, firestore
import os

# pip install --upgrade firebase-admin

# Use a service account and generate json
cred = credentials.Certificate(
    os.path.dirname(os.path.abspath(__file__)) + "/../auth/auth.json"
)

# Initialize
app = firebase_admin.initialize_app(cred)
db = firestore.client()


# Add Data
def add_data(collec, doc, data):
    if type(data) != type({}):
        print("Data must in dictionary format")
        return
    ref = db.collection(collec).document(doc)
    ref.set(data)


# Read Data
def read_data(collec, doc=""):
    if len(doc) != 0:
        ref = db.collection(collec).document(doc)
        doc = ref.get()
        if not doc.exists:
            print("Document does not exist")
            return
        return doc.to_dict()
    else:
        ref = db.collection(collec).stream()
        data = {}
        for doc in ref:
            data[doc.id] = doc.to_dict()
        return data


# Delete Data
def delete_data(collec, doc, fields=""):
    ref = db.collection(collec).document(doc)
    if type(fields) == type([]) and len(fields) != 0:
        param = {}
        for field in fields:
            param[field] = firestore.DELETE_FIELD
        ref.update(param)
        return
    if len(fields) == 0:
        db.collection(collec).document(doc).delete()
        return
    ref.update({fields: firestore.DELETE_FIELD})


# Update Data
def update_data(collec, doc, fields):
    if type(fields) != type({}):
        print("Fields must in dictionary format")
        return
    ref = db.collection(collec).document(doc)
    ref.update(fields)
