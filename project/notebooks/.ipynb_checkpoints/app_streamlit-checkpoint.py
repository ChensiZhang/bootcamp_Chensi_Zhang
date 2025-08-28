
import streamlit as st
import joblib

# 加载模型
model = joblib.load('model/model.pkl')

st.title("Model Prediction Dashboard")

# 输入特征
input_1 = st.number_input("Feature 1", value=0.0)
input_2 = st.number_input("Feature 2", value=0.0)

if st.button("Predict"):
    pred = model.predict([[input_1, input_2]])
    st.write(f"Prediction: {pred[0]}")
