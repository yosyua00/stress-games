import streamlit as st

st.title("シンプルなゲーム")
st.write("ボタンを押して開始！")

if st.button("Start Game"):
    st.write("ゲームが開始されました。")