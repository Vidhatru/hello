import streamlit as st
import firebase_admin
import matplotlib.pyplot as plt
import calendar
from firebase_admin import credentials, firestore
from collections import defaultdict
from datetime import date
if not firebase_admin._apps:
    cred1=credentials.Certificate("expense-tracker-3d8c7-firebase-adminsdk-fbsvc-cd5bde5936.json")
    firebase_admin.initialize_app(cred1)
db = firestore.client()
users_ref = db.collection("expenses")
total=0
def total_expense():
    users_ref = db.collection("expenses")
    docs = users_ref.stream()
    return[{"id":doc.id,**doc.to_dict()} for doc in docs]
def total_budgets():
    users_ref=db.collection("budgets")
    docs=users_ref.stream()
    return[{"id":doc.id,**doc.to_dict()} for doc in docs]
expenses=total_expense()
budgets=total_budgets()
st.title("Analytics Page")
month_names=["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
month=st.selectbox("Choose Month",month_names)
month_num=month_names.index(month)+1
first_day=date(2025,month_num,1)
last_day_num = calendar.monthrange(2025, month_num)[1]
last_day=date(2025,month_num,last_day_num)
count=0
expense_list=[]
category_totals={}
for i,expense in enumerate(expenses):
    expense_date=expense["Date"].date()
    if first_day<=expense_date and last_day>=expense_date:
        total+=expense["Amount"]
        count+=1
        expense_list.append(expense["Amount"])
        if expense["Category"] in category_totals:
            category_totals[expense["Category"]]+=expense["Amount"]
        else:
            category_totals[expense["Category"]]=expense["Amount"]
highest_expense=max(expense_list)
lowest_expense=min(expense_list)
avg_expense=total/count
highest_value=max(category_totals.values())
lowest_value=min(category_totals.values())
for key,value in category_totals.items():
    if value==highest_value:
        highest_category=key
        break
for key,value in category_totals.items():
    if value==lowest_value:
        lowest_category=key
        break
analytics_data=[
    {"Metric":f"💹 Total Expense in {month}","Value":f"₹{total}"},
    {"Metric":f"⬇️ Highest Category Spent in {month}","Value":highest_category},
    {"Metric":f"⬆️ Lowest Category Spent in {month}","Value":lowest_category},
    {"Metric":f"📉 Highest Transaction in {month}","Value":f"₹{highest_expense}"},
    {"Metric":f"📈 Lowest Transaction in {month}","Value":f"₹{lowest_expense}"},
    {"Metric":f"📃 Average Expense {month}","Value":f"₹{avg_expense}"}
]
st.table(analytics_data)
exceeded_categories=[]
for i,budget in enumerate(budgets):
    if budget   ["Budget_Month"]==month:
        category=budget["Budget"]
        budget_amount = budget["Budget_Amount"]
        spent=category_totals.get(category,0)
        if spent>budget_amount:
            exceeded_categories.append({
                f"Categories Exceeded for {month}": category,
                f"Budget for {month}": budget_amount,
                f"Amount Spent in {month}": f"₹{spent}",
                f"Amount Exceeded in {month}": f"₹{spent-budget_amount}"
            })
st.header("Categories Exceeding Budget")
st.table(exceeded_categories)
if category_totals:
    labels=list(category_totals.keys())
    sizes=list(category_totals.values())
    fig,ax=plt.subplots()
    ax.pie(sizes,labels=labels,autopct='%1.1f%%',startangle=90)
    ax.axis("equal")
    ax.set_title(f"Expenses According to Category For {month}")
    st.pyplot(fig)
else:
    st.write(f"No expense data available for {month}")
