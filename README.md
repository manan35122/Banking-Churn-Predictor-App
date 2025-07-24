# 🏦 Banking Customer Churn Predictor

This is a machine learning-powered web application built with **Streamlit** that predicts whether a banking customer is likely to churn based on their input features.

## 🚀 Features

- Predicts customer churn using a trained Logistic Regression model
- Interactive and user-friendly web interface
- Scales input features for accurate predictions
- Fast, real-time results

## 📊 Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Joblib

## 📁 Project Structure

```
banking-churn-predictor-app/
├── app.py                  # Main Streamlit app
├── model.joblib            # Trained machine learning model
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 🧠 How it Works

1. User provides input values such as Credit Score, Age, Geography, Gender, etc.
2. The input features are scaled using the same method used during training.
3. The trained logistic regression model predicts whether the customer will churn.
4. The prediction (Yes/No) and churn probability are shown.

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/manan35122/Banking-Churn-Predictor-App
cd banking-churn-predictor-app
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate        # Windows
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

## 📌 Note

- The model was trained using scaled features, so input data is scaled before prediction.
- One-hot encoding is used for `Geography` and `Gender`.
- Visit [App Link](https://manan35122-banking-churn-predictor-app-app-1bvq9u.streamlit.app/)

## ✍️ Author

**Manan**  
📫 [[LinkedIn](https://www.linkedin.com/in/abdulmanan-arshad)]  
💬 Built as part of a machine learning deployment project using Streamlit.
