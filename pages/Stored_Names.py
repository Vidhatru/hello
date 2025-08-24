import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
if not firebase_admin._apps:
    cred1=credentials.Certificate("hello-744b5-firebase-adminsdk-fbsvc-7a93d1a4c1.json")
    firebase_admin.initialize_app(cred1)
db = firestore.client()
above_10=[]
def get_all_ages_above_10():
    users_ref = db.collection("users")
    docs = users_ref.stream()
    for doc in docs:
        data=doc.to_dict()
        if data["age"]>10:
            above_10.append(data)
    return above_10
st.title("Users with age above 10")
users=get_all_ages_above_10()
for user in users:
    st.table(user)
if st.button("Clear"):
    users_ref = db.collection("users")
    docs = users_ref.stream()
    for doc in docs:
        doc.reference.delete()
    st.success("All users have been deleted")

 

