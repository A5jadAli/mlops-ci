import streamlit as st

# Title
st.title("Calculator Application")
st.subheader("Perform basic arithmetic operations easily!")

# Input numbers
num1 = st.number_input("Enter the first number:", value=0.0, step=0.1)
num2 = st.number_input("Enter the second number:", value=0.0, step=0.1)

# Select operation
operation = st.selectbox(
    "Choose an operation:",
    ["Addition", "Subtraction", "Multiplication", "Division"]
)

# Perform calculation
result = None
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Division by zero is not allowed!")
    
    if result is not None:
        st.success(f"The result of {operation} is: {result}")

# Sidebar
st.sidebar.title("About")
st.sidebar.info("This is a simple calculator built with Streamlit.")