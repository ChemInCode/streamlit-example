import streamlit as st

try:
    st.write('''<iframe src="http：//www.baidu.com" width="800px" height="600px"></iframe>''', unsafe_allow_html=True)
except Exception as e:
    st.write(e)
