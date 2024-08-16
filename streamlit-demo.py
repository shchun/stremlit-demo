from dotenv import load_dotenv
import streamlit as st
import openai
import os
from langchain.chat_models import ChatOpenAI

load_dotenv()

# ChatGPT API 호출
def call_chatgpt_api(message):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    chat_model = ChatOpenAI()

    res = chat_model.predict(message + "로 시조를 지어줘.")
    return res


def main():
    st.title("ChatGPT 예제")
    user_input = st.text_input("단어를 입력하세요", "")
    if user_input:

        # 사용자 입력 받기
        chatgpt_response = call_chatgpt_api(user_input)

        st.write(f"ChatGPT 응답: {user_input}에 대한 답변입니다.")
        st.write(f"ChatGPT 응답: {chatgpt_response}")
if __name__ == "__main__":
    main()