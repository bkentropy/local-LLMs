from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="llama3.1:8b")

chain = prompt | model

for chunk in chain.stream({"question": "What is LangChain?"}):
    print(chunk, end="", flush=True)
print()
