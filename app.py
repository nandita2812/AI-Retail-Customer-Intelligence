import streamlit as st
import pandas as pd

st.title("AI Retail Dashboard")

# Load data
rfm = pd.read_csv("outputs/rfm_final.csv")
reco = pd.read_csv("outputs/final_recommendations.csv")

# Show customer data
st.subheader("Customer Data")
st.write(rfm.head())

# Show segments
st.subheader("Customer Segments")
st.bar_chart(rfm['Segment'].value_counts())

# Show recommendations
st.subheader("Product Recommendations")
st.write(reco.head())


st.subheader("Find Product Recommendations")
product = st.text_input("Enter product name")
if product:
    result = reco[reco['antecedents'].str.contains(product, case=False)]
    st.write(result.head())


# Add Churn chart
st.subheader("Churn Distribution")
st.bar_chart(rfm['Churn'].value_counts())

# improving ui
st.title("AI-Powered Retail Customer Intelligence System")
st.markdown("---")

#to show top best customers
st.subheader("Top Customers")
top_customers = rfm.sort_values(by='Monetary', ascending=False).head(10)
st.write(top_customers)


# Customer Spendings
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.hist(rfm['Monetary'], bins=30)
st.pyplot(fig)

# Shows relationship between Customer
st.subheader("Recency vs Frequency")
fig, ax = plt.subplots()
ax.scatter(rfm['Recency'], rfm['Frequency'])
ax.set_xlabel("Recency")
ax.set_ylabel("Frequency")
st.pyplot(fig)

# Adding  Download Button 

st.download_button(
    label="Download Recommendations",
    data=reco.to_csv(index=False),
    file_name="recommendations.csv",
    mime="text/csv"
)