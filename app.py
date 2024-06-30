from pandasai.llm.local_llm import LocalLLM
import streamlit as st 
from pandasai.connectors import MySQLConnector
from pandasai import SmartDataframe

my_connector = MySQLConnector(
    config = {
        "host":"localhost",
        "port":3306,
        "database":"dados_fatura",
        "username":"root",
        "password":"admin",
        "table":"bike_sales_data",
    }
)

model = LocalLLM(
    api_base = "http://localhost:11434/v1",
    model = "llama3"
)

df_connector = SmartDataframe(my_connector, config = {"llm": model})

st.title("CHATBOT WITH MY DATABASE")

with st.sidebar:
    st.subheader("Settings")
    st.write("This is a generative database project. ")
    
    st.text_input('Host', value = 'localhost', key = 'host')
    st.text_input('Port', value = '3306', key = 'port')
    st.text_input('User', value = 'root', key = 'username')
    st.text_input('Password', type = 'password', value = 'admin', key = 'password')
    st.text_input('Database', value = 'bike_sales_data', key = 'table')
    if st.button("Conectar"):
        with st.spinner('Connecting with the database...'):
            db = my_connector

            st.session_state.db = db
            st.success('Connected to database!')

prompt = st.text_input("Enter your prompt:")

if st.button("Generate"):
    if prompt:
        with st.spinner("Generating response..."):
            st.write(df_connector.chat(prompt))