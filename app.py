import streamlit as st
import pandas as pd
import json
import time
from confluent_kafka import Consumer

st.set_page_config(
    page_title="Real-Time Fraud Detection",
    page_icon="💳",
    layout="wide"
)

st.title("💳 Real-Time Financial Fraud Detection")
st.caption("Powered by Python | Apache Kafka | Streamlit")

if "consumer" not in st.session_state:
    st.session_state.consumer = Consumer({
        "bootstrap.servers": "localhost:9092",
        "group.id": "dashboard-fraud-group",
        "auto.offset.reset": "latest"
    })
    st.session_state.consumer.subscribe(["transactions"])

if "transactions" not in st.session_state:
    st.session_state.transactions = []

@st.fragment(run_every=2)
def live_dashboard():
    consumer = st.session_state.consumer

    for _ in range(10):
        msg = consumer.poll(0.1)

        if msg is None or msg.error():
            continue

        data = json.loads(msg.value().decode("utf-8"))
        amount = data["amount"]

        st.session_state.transactions.append({
            "User ID": data["user_id"],
            "Amount ($)": amount,
            "Status": "Suspicious" if amount > 1000 else "Normal",
            "Time": time.strftime("%H:%M:%S")
        })

    df = pd.DataFrame(
        st.session_state.transactions,
        columns=["User ID", "Amount ($)", "Status", "Time"]
    )

    total = len(df)
    fraud_df = df[df["Status"] == "Suspicious"]
    normal_df = df[df["Status"] == "Normal"]

    fraud = len(fraud_df)
    normal = len(normal_df)
    fraud_percentage = (fraud / total * 100) if total else 0

    st.subheader("📊 Transaction Analytics")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Transactions", total)
    col2.metric("Suspicious", fraud)
    col3.metric("Normal", normal)
    col4.metric("Fraud Rate", f"{fraud_percentage:.1f}%")

    st.divider()

    if total:
        left, right = st.columns(2)

        with left:
            st.subheader("Transaction Status")
            status_data = pd.DataFrame({
                "Count": [normal, fraud]
            }, index=["Normal", "Suspicious"])
            st.bar_chart(status_data)

        with right:
            st.subheader("Transaction Amounts")
            st.line_chart(df["Amount ($)"])

        st.divider()

        st.subheader("🚨 Fraud Alert History")

        if fraud:
            st.error(f"{fraud} suspicious transactions detected!")
            st.dataframe(fraud_df.tail(20), use_container_width=True)
        else:
            st.success("No suspicious transactions detected.")

        st.subheader("📋 All Live Transactions")
        st.dataframe(df.tail(50), use_container_width=True)

    else:
        st.info("Waiting for Kafka transactions...")

live_dashboard()