#create-qas.py
# Create QAs using LLMs (LM Studio) LangChain

# We need to start with document splitting.

with open('Book-In-Text.txt', 'r') as file:
    data = file.read()

from langchain.text_splitter import RecursiveCharacterTextSplitter

r_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=250,
    separators=["\n\n", "\n", "(?<=\. )", " ", ""]
)
new_data = r_splitter.split_text(data)


# print every entry of the list on a new line
for item in new_data:
    print('-------------------------------------------------------------------------------------------------------------------')
    print(item)


print(len(new_data))


# from langchain.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI

# llm_model = ChatOpenAI(temperature=0.0, base_url="http://localhost:1234/v1", api_key="not-needed")


# with open('Book-In-Text.txt', 'r') as file:
#     data = file.read()
# #print(data)


# from langchain.evaluation.qa import QAGenerateChain

# # example_gen_chain = QAGenerateChain.from_llm(llm=llm_model)
# # new_examples = example_gen_chain.apply_and_parse(
# #     [{"doc": t} for t in data[:5]]
# # )

# print([{"doc": t} for t in data[:5]])
# print()