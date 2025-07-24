import streamlit as st
import numpy as np
import pandas as pd
import joblib as jb

st.title("🏦 Bank Customer Churn Prediction")
model = jb.load("Model.joblib")
scaler = jb.load('scaler.joblib')

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
st.markdown("Displaying only first 5 rows")
df = pd.read_csv("Churn_Modelling.csv")
st.dataframe(df.head())

st.header("Cleaned Dataset Used for Training")
st.markdown("Displaying only first 5 rows")
df = pd.read_csv("cleaned_data.csv")
df['HasCrCard'] = df["HasCrCard"].fillna(1)
df['IsActiveMember'] = df["IsActiveMember"].fillna(1)
df['Age'] = df["Age"].fillna(df["Age"].median())
st.dataframe(df.head())
st.markdown("---")
st.header("Now lets predict for you ;)")
cr_score = st.number_input("Credit Score",0,1000)
age = st.number_input("Age:", 18,110)
tenure = st.number_input("Tenure with Bank:", 0.0,20.0)
balance = st.number_input('Balance:' , 0.0 , 3000000.0)
NumProduct = st.number_input('Number of Products' , 0 , 10)
CrCard = st.selectbox('Has Credit Card:',('No' , 'Yes'))
CrCard = 1 if CrCard == 'Yes' else 0
isActive = st.selectbox('Is Active Member?',('Yes','No'))
isActive = 1 if isActive == 'Yes' else 0
estimatedSalary = st.number_input('Estimated Salary($):' , 0.0)
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.selectbox("Gender", ["Male", "Female"])

geo_germany = 1 if geography == "Germany" else 0
geo_spain = 1 if geography == "Spain" else 0  


gender_male = 1 if gender == "Male" else 0 
st.markdown("---")
st.header("Details:")
st.write('Credit Score: ', cr_score)
st.write('Age: ',age)
st.write('Tenure: ',tenure)
st.write('Balance: ',balance)
st.write('Number of Products: ',NumProduct)
st.write('Credit Card' , 'Yes' if CrCard == 1 else 'No')
st.write("Active Member: ", 'Yes' if isActive == 1 else 'No')
st.write('Estimated Salary: ',estimatedSalary)

if st.button("Predict"):
    features = np.array([[cr_score, age, tenure, balance, NumProduct,
                          CrCard, isActive, estimatedSalary,
                          geo_germany, geo_spain, gender_male]])

    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    prob = model.predict_proba(features_scaled)[0][1]
    st.subheader("Prediction")
    st.write("🚨 Customer **WILL CHURN**." if prediction == 1 else "✅ Customer **WILL NOT CHURN**.")
    st.write(f"📊 Churn Probability: **{prob:.2%}**")


st.markdown("---")
st.markdown("### About the Developer")
st.markdown("If you liked this app or have suggestions, feel free to reach out!")
st.markdown("**Email**: mananarshad351@gmail.com")
st.link_button("Github", 'https://github.com/manan35122')
st.link_button("LinkedIn", 'https://www.linkedin.com/in/abdulmanan-arshad')

