# calculator.py
import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b

# Streamlit Application
st.title("Calculator Application")
st.subheader("Perform basic arithmetic operations easily!")

num1 = st.number_input("Enter the first number:", value=0.0, step=0.1)
num2 = st.number_input("Enter the second number:", value=0.0, step=0.1)
operation = st.selectbox("Choose an operation:", ["Addition", "Subtraction", "Multiplication", "Division"])

result = None
if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = add(num1, num2)
        elif operation == "Subtraction":
            result = subtract(num1, num2)
        elif operation == "Multiplication":
            result = multiply(num1, num2)
        elif operation == "Division":
            result = divide(num1, num2)
        st.success(f"The result of {operation} is: {result}")
    except ValueError as e:
        st.error(str(e))

st.sidebar.title("About")
st.sidebar.info("This is a simple calculator built with Streamlit.")