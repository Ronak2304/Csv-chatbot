import streamlit as st
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="FinFlow: ")
    st.header("Welcome to FinBot")
    user_csv = st.file_uploader("Upload your CSV file: ",type="csv")

    if user_csv is not None:
        user_question = st.text_input("Ask anything : ")

    llm = OpenAI(temperature=1)
    agent = create_csv_agent(llm,user_csv,verbose=False,allow_dangerous_code=True)

    if user_question is not None and user_question != "":
        response = agent.run(user_question)
        st.write(response)
if __name__ == "__main__":
    main()