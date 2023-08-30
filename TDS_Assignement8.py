#pip install -q streamlit
import streamlit as st

st.text("Hello Raj Mogli")

st.title("Find the Largest Number")
num1 = st.number_input("Enter the first number:")
num2 = st.number_input("Enter the second number:")
num3 = st.number_input("Enter the third number:")

#largest = find_largest(num1, num2, num3)
largest = max(num1, num2, num3)
st.write("The largest number is: {largest}")
