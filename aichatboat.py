import streamlit as st
import google.generativeai as genai
import pandas as pd
import matplotlib.pyplot as plt
with st.sidebar:
    st.title("MENU")
    section = st.radio("Choose Section:",
                       ["Profile", "Library", "Virtual Assistant"])
    st.write("Created by Shivam Kumar")
if section == "Profile":
    st.header("My Profile")
    st.write("Name: Shivam Kumar")
    st.write("Location: Jaipur, India")
    st.write("Skills: Python, Java, C, Generative AI")
    st.image(r"C:\Users\SHIVAM KUMAR\Downloads\python_practics\project\appnaa.jpg", caption="Profile Photo")
elif section == "Library":
    st.header("Tools")
    st.subheader("Bar Chart Example")
    chart_data = pd.DataFrame({"marks": [10, 20, 30, 10]})
    st.line_chart(chart_data)
    st.bar_chart(chart_data)
    st.subheader("Pie Chart Example")
    subject = ["Python", "C++", "Java"]
    marks = [20, 10, 5]
    fig, ax = plt.subplots()
    ax.pie(marks, labels=subject, autopct='%1.1f%%')
    st.pyplot(fig)
    st.title("Bubble Chart Example in Streamlit")
    x = [10, 20, 30, 40, 50]
    y = [5, 25, 15, 35, 10]
    sizes = [100, 200, 300, 500, 400]
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=sizes, alpha=0.5)
    ax.set_title("Bubble Chart")
    ax.set_xlabel("X Values")
    ax.set_ylabel("Y Values")
    st.pyplot(fig)
    st.subheader("Simple Calculator")
    num1 = st.number_input("Enter first number", value=0)
    num2 = st.number_input("Enter second number", value=0)
    operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])
    if st.button("Calculate"):
        if operation == "Add":
            st.success(f"Result: {num1 + num2}")
        elif operation == "Subtract":
            st.success(f"Result: {num1 - num2}")
        elif operation == "Multiply":
            st.success(f"Result: {num1 * num2}")
        elif operation == "Divide":
            st.success(f"Result: {num1 / num2 if num2 != 0 else 'Error: Division by zero'}")

elif section == "Virtual Assistant":
    st.header("🤖 Virtual Assistant")
    st.text("Welcome to my dashboard!")

    API_KEY = "enter your api no"  
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-2.5-flash")

    user_msg = st.text_input("Enter your text :")
    if st.button("Send Message"):
        if user_msg.strip() != "":
            with st.spinner("Generating response..."):
                response = model.generate_content(user_msg)
            st.success("Bot Response:")
            st.write(response.text)
