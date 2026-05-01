import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


if 'expense' not in st.session_state:
    st.session_state.expense = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])


def add_expense(date, category, amount, description):
    new_expense = pd.DataFrame([[date, category, amount, description]],
                               columns=st.session_state.expense.columns)
    st.session_state.expense = pd.concat(
        [st.session_state.expense, new_expense],
        ignore_index=True
    )

def load_expense():
    uploaded_file = st.file_uploader("Choose a file", type=['csv'])
    if uploaded_file is not None:
        st.session_state.expense = pd.read_csv(uploaded_file)

def save_expense():
    st.session_state.expense.to_csv('expense.csv', index=False)
    st.success("Expense saved successfully")

def vizualize_expense():
    if not st.session_state.expense.empty:
        fig, ax = plt.subplots()
        sns.barplot(data=st.session_state.expense, x="Category", y="Amount", ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.warning("No Expense to Vizualize")


st.title('Expense Tracker')

with st.sidebar:
    st.header('Add Expense')
    date = st.date_input("Date")
    category = st.selectbox('Category',['Food','Transport','Entertainment','Utility','Other'])
    amount = st.number_input('Amount', min_value=0.0, format="%.2f")
    description = st.text_input('Description')

    if st.button('Add'):
        add_expense(date, category, amount, description)
        st.success("Expense Added")

    st.header('File Operation')

    if st.button('Save Expense'):
        save_expense()

   
    uploaded_file = st.file_uploader("Load CSV", type=['csv'])
    if uploaded_file is not None:
        st.session_state.expense = pd.read_csv(uploaded_file)


st.header('Expense')
st.write(st.session_state.expense)

st.header('Visualization')
if st.button('Vizualize Expense'):
    vizualize_expense()