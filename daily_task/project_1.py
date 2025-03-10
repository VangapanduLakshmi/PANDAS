
import streamlit as st
s = st.text_input("enter you input")
res = s[::-1]
if st.button("clik me"):
    if res ==s:
        st.write("palindrome")
        st.balloons()
    else:
        st.write("not palindrome")
        st.snow()