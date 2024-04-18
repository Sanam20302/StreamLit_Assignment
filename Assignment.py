import streamlit as st
import numpy as np
st.title("Graded Assignment Week - 8")
num1 = st.number_input('Enter the first number')
num2 = st.number_input('Enter the second number')
num3 = st.number_input('Enter the third number')
st.write(max([num1,num2,num3]))
