import streamlit as st

st.title("Addition of Two Numbers")

num1 = st.number_input("Input First Number", format="%g")
num2 = st.number_input("Input Second Number", format="%g")
total = num1 + num2

if st.button("Add"):
    st.write("({}) + ({})  =  {}".format(num1, num2, total))
    st.write("Addition of numbers {} and {} is equals to {}".format(num1, num2, total))
