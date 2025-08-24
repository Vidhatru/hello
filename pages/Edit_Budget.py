import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import date,datetime
if not firebase_admin._apps:
    cred1=credentials.Certificate("hello-744b5-firebase-adminsdk-fbsvc-7a93d1a4c1.json")
    firebase_admin.initialize_app(cred1)
db = firestore.client()
st.title("View Budget")
budget_id=st.query_params.get("id")    
doc_ref = db.collection("budgets").document(budget_id)
doc=doc_ref.get()
budget=doc.to_dict()
categories=["Housing","Utilities","Clothing","Insurance","Transportation","Food","Entertainment","Others"]
if budget is not None and "Budget" in budget and budget["Budget"] in categories:
    if budget["Budget"] in categories:
        categories.remove(budget["Budget"])
    new_categories=[budget["Budget"]]+categories
    new_budget=st.radio("Change the category of expense",new_categories)
    month=["January","February","March","April","May","June","July","August","September","October","November","December"]
    new_month=st.selectbox("Select Month",month)
    new_budgetamount=st.number_input("Change Amount",value=budget["Budget_Amount"])
    if st.button("✅ Save Changes"):
        doc_ref.set({
            "Budget":new_budget,
            "Budget_Amount":new_budgetamount,
            "Budget_Month":new_month,
        })
        st.success("Changes have been saved!")
    if st.button("❌ Delete"):
        doc.reference.delete()
        st.success("Data has been deleted!")
        st.switch_page("pages/Display_Budgets.py")
    if st.button("🔙 Go Back"):
        st.switch_page("pages/Display_Budgets.py")
else:
    st.error("Expense not found.")








