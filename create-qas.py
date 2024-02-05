#create-qas.py
# Create QAs using LLMs (LM Studio) LangChain


from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

chat = ChatOpenAI(temperature=0.0, base_url="http://localhost:1234/v1", api_key="not-needed")

