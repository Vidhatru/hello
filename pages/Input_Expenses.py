import streamlit as st
import firebase_admin
import calendar 
from firebase_admin import credentials, firestore
from datetime import date,datetime
if not firebase_admin._apps:
    cred1=credentials.Certificate("expense-tracker-3d8c7-firebase-adminsdk-fbsvc-cd5bde5936.json")
    firebase_admin.initialize_app(cred1)
db = firestore.client()
st.title("Expense Tracker")
def add_expense(name,amount,Date,desc):
    doc_ref = db.collection("expenses").document()
    date_obj = datetime.combine(Date, datetime.min.time())
    doc_ref.set({
        "Category": name,
        "Amount": amount,
        "Date": date_obj,
        "Desc": desc
    })
def total_expense():
    users_ref=db.collection("expenses")
    docs=users_ref.stream()
    return[{"id":doc.id,**doc.to_dict()} for doc in docs]
expenses=total_expense()
def total_budgets():
    users_ref=db.collection("budgets")
    docs=users_ref.stream()
    return[{"id":doc.id,**doc.to_dict()} for doc in docs]
budgets=total_budgets()
name=st.radio("Chooses the category of expense",
              ("Housing","Utilities","Clothing","Insurance","Transportation","Food","Entertainment","Others"))
amount=st.number_input("Enter the expense")
Date=st.date_input("Enter the date")
desc=st.text_input("Description")
month_name=calendar.month_name[Date.month]
for i,budget in enumerate(budgets):
    if month_name==budget["Budget_Month"] and name==budget["Budget"]:
        total=0
        for i, expense in enumerate(expenses):
            Amount_Date=expense["Date"].date()
            Amount_Month=calendar.month_name[Amount_Date.month]
            if budget["Budget_Month"]==Amount_Month and budget["Budget"]==expense["Category"]:
                total+=expense["Amount"]
        total+=amount
        if total>budget["Budget_Amount"]:
            st.error("You are exceeding your budget limit, Do you still wish to continue?")
        break
if st.button("➕ Add Expense"):
    add_expense(name,amount,Date,desc)
    st.success("The amount has been successfully stored!")
if st.button("📑 See All Expenses"):
    st.switch_page("pages/Display_Expenses.py")

