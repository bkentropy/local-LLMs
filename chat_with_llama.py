from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.1:8b")
# model = OllamaLLM(model="qwen2.5-coder:1.5b-base")

chain = prompt | model

response = chain.invoke({"question": "What is LangChain?"})
print(response)
