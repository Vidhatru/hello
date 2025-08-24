import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import date,datetime
if not firebase_admin._apps:
    cred1=credentials.Certificate("hello-744b5-firebase-adminsdk-fbsvc-7a93d1a4c1.json")
    firebase_admin.initialize_app(cred1)
db = firestore.client()
st.title("Budget Setter")
def set_budget(budget,budget_month,budget_amount):
    doc_ref = db.collection("budgets").document()
    doc_ref.set({
        "Budget": budget,
        "Budget_Month": budget_month,
        "Budget_Amount": budget_amount
    })

budget=st.radio("Set Budget for Categories",
              ("Housing","Utilities","Clothing","Insurance","Transportation","Food","Entertainment","Others"))
month=["January","February","March","April","May","June","July","August","September","October","November","December"]
budget_month=st.selectbox("Select Month",month)
budget_amount=st.number_input("Enter the budget")
if st.button("👍 Save Changes"):
    set_budget(budget,budget_month,budget_amount)
    st.success("The budget has been successfully set!")
if st.button("📑 See All Budgets"):
    st.switch_page("pages/Display_Budgets.py")