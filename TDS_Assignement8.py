import streamlit as st

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest Number")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    if st.button("Find Largest"):
        largest = find_largest(num1, num2, num3)
        st.write(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
To run this code, make sure you have Streamlit installed (pip install streamlit), and then save the code to a .py file (e.g., largest_number_app.py). Open your terminal, navigate to the directory where the file is saved, and run the following command:

arduino
Copy code
streamlit run largest_number_app.py
This will open a new browser tab with your Streamlit app where you can input the three numbers and find the largest among them.

After you have developed and tested your Streamlit application, you can follow Streamlit Cloud's documentation to deploy your app to their platform and obtain a URL.





