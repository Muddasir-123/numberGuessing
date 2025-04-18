import streamlit as st
from random import randint 
st.title("Number Guessing Game🤔.")
st.write("Guess the number between 1 to 10.")
user_num=st.number_input("Guess?",value=0)
com_num=randint(1,10)
def guess(user_num,com_num):
    if user_num == com_num:
        st.success("You Won")
        st.balloons()
    elif user_num >com_num:
        st.warning(f"Com number is less than your number. {com_num}")
    elif user_num < com_num:
        st.warning(f"Computer number is greater than your number. {com_num}")
if st.button("Guess"):
    guess(user_num,com_num)