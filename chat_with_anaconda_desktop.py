# use OpenAI compatible API
# you can test with: curl 192.168.1.14:8080/v1/models
# langchain is good here, use that to write a simple "hello world" chat

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# Configure the chat model to use the local OpenAI-compatible API
llm = ChatOpenAI(
    base_url="http://192.168.1.14:8080/v1",
    api_key="DUMMY",  # Local API doesn't require a real key
    model="default",  # Use the default model from the local server
    temperature=0.7,
)

# Simple hello world chat
def hello_world_chat():
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content="Hello! Can you say hello world?"),
    ]
    print(f"lenght of messages: {len(messages)}")
    
    response = llm.invoke(messages)
    print(f"Assistant: {response.content}")

if __name__ == "__main__":
    hello_world_chat()
