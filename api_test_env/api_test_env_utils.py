import requests
import streamlit as st

# FastAPIのエンドポイントURL
# FASTAPI_URL = "http://127.0.0.1:8000/process"
FASTAPI_URL = 'http://localhost:8000/'

# Streamlitで入力を受け取る
input_value = st.text_input("Enter a value:")

if st.button("Process"):
    # FastAPIにリクエストを送信
    response = requests.get(FASTAPI_URL, params={"input_value": input_value})

    if response.status_code == 200:
        result = response.json()
        st.write(f"Original: {result['original']}")
        st.write(f"Processed: {result['processed']}")
    else:
        st.write("Error: Unable to process the input")

# if __name__ == "__main__":
#     st.
