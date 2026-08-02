import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Expense Tracker",
    page_icon="💰",
    layout="wide"
)
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

#def save_expense():
   # st.session_state.expense.to_csv('expense.csv', index=False)
   # st.success("Expense saved successfully")

def vizualize_expense():
    if not st.session_state.expense.empty:
        fig, ax = plt.subplots()
        sns.barplot(data=st.session_state.expense, x="Category", y="Amount", ax=ax)
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.warning("No Expense to Vizualize")
st.markdown("""
<style>

div[data-testid="metric-container"]{
    background:#1E293B;
    border:1px solid #334155;
    padding:18px;
    border-radius:16px;
    transition:0.3s;
}

div[data-testid="metric-container"]:hover{
    transform:translateY(-4px);
    border:1px solid #22C55E;
    box-shadow:0 8px 20px rgba(34,197,94,0.25);
}

section[data-testid="stSidebar"]{
    background:#111827;
}

section[data-testid="stSidebar"] .stButton > button{
    background:#22C55E;
    color:white;
    border:none;
    border-radius:10px;
}

section[data-testid="stSidebar"] .stButton > button:hover{
    background:#16A34A;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

div[data-testid="metric-container"]{
    background:#1E293B;
    border:1px solid #334155;
    padding:18px;
    border-radius:16px;
    transition:0.3s;
}

div[data-testid="metric-container"]:hover{
    transform:translateY(-4px);
    border:1px solid #22C55E;
    box-shadow:0 8px 20px rgba(34,197,94,0.25);
}

section[data-testid="stSidebar"]{
    background:#111827;
}

section[data-testid="stSidebar"] .stButton > button{
    background:#22C55E;
    color:white;
    border:none;
    border-radius:10px;
}

section[data-testid="stSidebar"] .stButton > button:hover{
    background:#16A34A;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<div style="
background:linear-gradient(90deg,#0F172A,#1E293B);
padding:35px;
border-radius:18px;
border-left:6px solid #22C55E;
margin-bottom:30px;
text-align:center;
">

<h1 style="
color:white;
font-size:42px;
margin-bottom:8px;
">
💰 Personal Expense Tracker
</h1>

<p style="
color:#CBD5E1;
font-size:18px;
margin-bottom:25px;
">
Track • Analyze • Save Smarter
</p>

<div style="
display:flex;
justify-content:center;
gap:12px;
flex-wrap:wrap;
">

<span style="
background:#334155;
padding:10px 18px;
border-radius:30px;
color:white;
">
📊 Analytics
</span>

<span style="
background:#334155;
padding:10px 18px;
border-radius:30px;
color:white;
">
💵 Budget
</span>

<span style="
background:#334155;
padding:10px 18px;
border-radius:30px;
color:white;
">
📈 Insights
</span>

<span style="
background:#334155;
padding:10px 18px;
border-radius:30px;
color:white;
">
📂 CSV Support
</span>

</div>

</div>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# KPI CALCULATIONS
# ---------------------------------------------------

if not st.session_state.expense.empty:

    total_expense = st.session_state.expense["Amount"].sum()

    total_transactions = len(st.session_state.expense)

    total_categories = st.session_state.expense["Category"].nunique()

    avg_expense = st.session_state.expense["Amount"].mean()

else:

    total_expense = 0
    total_transactions = 0
    total_categories = 0
    avg_expense = 0

# ---------------------------------------------------
# KPI DASHBOARD
# ---------------------------------------------------

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "💰 Total Spending",
        f"₹ {total_expense:,.2f}"
    )

with c2:
    st.metric(
        "🧾 Transactions",
        total_transactions
    )

with c3:
    st.metric(
        "📂 Categories",
        total_categories
    )

with c4:
    st.metric(
        "📊 Average Expense",
        f"₹ {avg_expense:,.2f}"
    )

st.markdown("<br>", unsafe_allow_html=True)

with st.sidebar:

    st.markdown("## 💰 Expense Tracker")

    st.caption("Track • Analyze • Save Smarter")

    st.markdown("---")

    st.markdown("### ➕ Add New Expense")

    date = st.date_input("📅 Date")

    category = st.selectbox(
        "📂 Category",
        [
            "Food",
            "Transport",
            "Entertainment",
            "Utility",
            "Other"
        ]
    )

    amount = st.number_input(
        "💵 Amount",
        min_value=0.0,
        format="%.2f"
    )

    description = st.text_input(
        "📝 Description"
    )

    if st.button("➕ Add Expense"):
        add_expense(
            date,
            category,
            amount,
            description
        )
        st.success("Expense Added Successfully!")

    st.markdown("---")

    st.markdown("### 📂 Import Data")

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if uploaded_file is not None:
        st.session_state.expense = pd.read_csv(uploaded_file)
        st.success("CSV Loaded Successfully!")

    st.markdown("---")

    st.markdown("### 📊 Quick Overview")

    st.metric(
        "💰 Total Spending",
        f"₹ {total_expense:,.0f}"
    )

    st.metric(
        "🧾 Transactions",
        total_transactions
    )

    st.markdown("---")

    st.markdown(
        """
        <div style="text-align:center;color:#94A3B8;font-size:14px;">
        Built with ❤️ using<br>
        <b>Python • Streamlit • Pandas</b>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("## 📋 Recent Transactions")

if st.session_state.expense.empty:

    st.info("No expenses added yet.")

else:

    st.dataframe(
        st.session_state.expense,
        use_container_width=True,
        hide_index=True
    )

st.header('Visualization')
if st.button('Vizualize Expense'):
    vizualize_expense()
