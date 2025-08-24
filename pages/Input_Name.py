import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
if not firebase_admin._apps:
    cred1=credentials.Certificate("hello-744b5-firebase-adminsdk-fbsvc-7a93d1a4c1.json")
    firebase_admin.initialize_app(cred1)

db = firestore.client()
def add_user(name, age):
    doc_ref = db.collection("users").document(name)
    doc_ref.set({
        "name": name,
        "age": age
    })

st.title("Enter student Name and Age ")

name = st.text_input("Enter name")
age = st.number_input("Enter age", min_value=0, max_value=120)

if st.button("Add User"):
    add_user(name, age)
    st.success(f"User {name} added")

    



