import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import date
if not firebase_admin._apps:
    cred1=credentials.Certificate("hexpense-tracker-3d8c7-firebase-adminsdk-fbsvc-cd5bde5936.json")
    firebase_admin.initialize_app(cred1)
db = firestore.client()
st.title("All Expenses")
expense_list=[]
def display_all_expenses():
    entries_ref = db.collection("expenses")
    docs = entries_ref.stream()
    return[{"id":doc.id,**doc.to_dict()} for doc in docs]
expenses=display_all_expenses()
h1,h2,h3,h4,h5=st.columns([1,1,1,1,1])
h1.subheader("S.NO")
h2.subheader("Name")
h3.subheader("Amount")
h4.subheader("Date")
h5.subheader("Action")
for i, expense in enumerate(expenses):
    col1,col2,col3,col4,col5=st.columns([1,1,1,1,1])
    col1.write(i+1)
    col2.write(expense["Category"])
    col3.write(expense["Amount"])
    col4.write(expense["Date"].date())
    col5.link_button(label=f"✏️Edit",url=f"/Edit_Expenses?id={expense["id"]}")
if st.button("➕ Add Expense"):
    st.switch_page("pages/Input_Expenses.py")
if st.button("🗑️ Clear All"):
    entries_ref=db.collection("expenses") 
    docs=entries_ref.stream()
    for doc in docs:
        doc.reference.delete()
    st.success("All Expenses Cleared")
    st.rerun()


    



