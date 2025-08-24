import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import date,datetime
if not firebase_admin._apps:
    cred1=credentials.Certificate("hello-744b5-firebase-adminsdk-fbsvc-7a93d1a4c1.json")
    firebase_admin.initialize_app(cred1)
db = firestore.client()
st.title("View Expense")
expense_id=st.query_params.get("id")    
doc_ref = db.collection("expenses").document(expense_id)
doc=doc_ref.get()
expense=doc.to_dict()
categories=["Housing","Utilities","Clothing","Insurance","Transportation","Food","Entertainment","Others"]
if expense is not None and "Category" in expense and expense["Category"] in categories:
    if expense["Category"] in categories:
        categories.remove(expense["Category"])
    new_categories=[expense["Category"]]+categories
    new_name=st.radio("Change the category of expense",new_categories)
    new_amount=st.number_input("Change Amount",value=expense["Amount"])
    new_date=st.date_input("Change Date",expense["Date"])
    new_desc=st.text_input("Change Description:",expense["Desc"])
    if st.button("✅ Save Changes"):
        date_obj = datetime.combine(new_date, datetime.min.time())
        doc_ref.set({
            "Category":new_name,
            "Amount":new_amount,
            "Date":date_obj,
            "Desc":new_desc
        })
        st.success("Changes have been saved!")
    if st.button("❌ Delete"):
        doc.reference.delete()
        st.success("Data has been deleted!")
        st.switch_page("pages/Display_Expenses.py")
    if st.button("🔙 Go Back"):
        st.switch_page("pages/Display_Expenses.py")
else:
    st.error("Expense not found.")








