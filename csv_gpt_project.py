import streamlit as st
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from dotenv import load_dotenv
from PIL import Image

def main():
    st.set_page_config(page_title="BridgeHealth Assistant")

    image = Image.open("/home/ananthkini/data/final_logo.png")

    st.image(image)

    load_dotenv()

    st.header("CSV Analyzer Assistant (CAA) - BridgeHealth")

    user_inp = st.text_input("Copy paste the path of your file here: ")

    filenames = []
    if user_inp is not None and user_inp != "":
        filenames.append(user_inp)

        user_question = st.text_input("Ask a question about your CSV File: ")

        llm = OpenAI(temperature=0.6)

        agent = create_csv_agent(llm, filenames, verbose = True)

        if user_question is not None and user_question != "":
            response = agent.run(user_question)
            st.write(response)


if __name__ == "__main__":
    main()