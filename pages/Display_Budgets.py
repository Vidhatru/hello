import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import date,datetime
if not firebase_admin._apps:
    cred1=credentials.Certificate("expense-tracker-3d8c7-firebase-adminsdk-fbsvc-cd5bde5936.json")
    firebase_admin.initialize_app(cred1)
db = firestore.client()
st.title("All Budgets")
budgets_list=[]
def display_all_budgets():
    entries_ref = db.collection("budgets")
    docs = entries_ref.stream()
    return[{"id":doc.id,**doc.to_dict()} for doc in docs]
budgets=display_all_budgets()
h1,h2,h3,h4,h5=st.columns([1,1,1,1,1])
h1.subheader("S.NO")
h2.subheader("Name")
h3.subheader("Amount")
h4.subheader("Month")
h5.subheader("Action")
for i, budget in enumerate(budgets):
    col1,col2,col3,col4,col5=st.columns([1,1,1,1,1])
    col1.write(i+1)
    col2.write(budget["Budget"])
    col3.write(budget["Budget_Amount"])
    col4.write(budget["Budget_Month"])
    col5.link_button(label=f"✏️Edit",url=f"/Edit_Budget?id={budget["id"]}")
if st.button("➕ Add Budget"):
    st.switch_page("pages/Budget.py")
if st.button("🗑️ Clear All"):
    entries_ref=db.collection("budgets") 
    docs=entries_ref.stream()
    for doc in docs:
        doc.reference.delete()
    st.success("All Expenses Cleared")
    st.rerun()