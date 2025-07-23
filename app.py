import streamlit as st
import numpy as np
import pandas as pd
import joblib

st.title("🏦 Bank Customer Churn Prediction")

st.markdown("""
The **bank customer churn dataset** is a commonly used dataset for predicting customer churn in the banking industry.  
It contains information on bank customers who either left the bank or continue to be a customer.

### 📄 Dataset Attributes:

- **Customer ID**: A unique identifier for each customer  
- **Surname**: The customer's surname or last name  
- **Credit Score**: A numerical value representing the customer's credit score  
- **Geography**: The country where the customer resides (France, Spain or Germany)  
- **Gender**: The customer's gender (Male or Female)  
- **Age**: The customer's age  
- **Tenure**: The number of years the customer has been with the bank  
- **Balance**: The customer's account balance  
- **NumOfProducts**: The number of bank products the customer uses (e.g., savings account, credit card)  
- **HasCrCard**: Whether the customer has a credit card (1 = yes, 0 = no)  
- **IsActiveMember**: Whether the customer is an active member (1 = yes, 0 = no)  
- **EstimatedSalary**: The estimated salary of the customer  
- **Exited**: Whether the customer has churned (1 = yes, 0 = no)
""")
st.header("Raw Dataset")
df = pd.read_csv("Churn_Modelling.csv")
st.dataframe(df)

st.header("Cleaned Dataset Used for Training")
df = pd.read_csv("cleaned_data.csv")
df['HasCrCard'] = df["HasCrCard"].fillna(1)
df['IsActiveMember'] = df["IsActiveMember"].fillna(1)
df['Age'] = df["Age"].fillna(df["Age"].median())
st.dataframe(df)

st.header("Now lets predict for you ;)")
cr_score = st.number_input("Credit Score",0,1000)
age = st.number_input("Age:", 18,110)
tenure = st.number_input("Tenure with Bank:", 0.0,20.0)
balance = st.number_input('Balance:' , 0.0 , 3000000.0)
NumProduct = st.number_input('Number of Products' , 0 , 10)
CrCard = st.selectbox('Has Credit Card:',('No' , 'Yes'))
CrCard = 1 if CrCard == 'Yes' else 0