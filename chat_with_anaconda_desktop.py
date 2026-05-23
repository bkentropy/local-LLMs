# use OpenAI compatible API
# you can test with: curl 192.168.1.14:8080/v1/models
# langchain is good here, use that to write a simple "hello world" chat

import typer
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

app = typer.Typer()

# Configure the chat model to use the local OpenAI-compatible API
llm = ChatOpenAI(
    base_url="http://192.168.1.14:8080/v1",
    api_key="DUMMY",  # Local API doesn't require a real key
    model="default",  # Use the default model from the local server
    temperature=0.7,
)

@app.command()
def chat():
    """Start a continuous conversation with the AI assistant."""
    typer.echo("Starting conversation with AI assistant (type 'quit' or 'exit' to stop)")
    typer.echo("-" * 50)
    
    conversation_history = [
        SystemMessage(content="You are a helpful assistant."),
    ]
    
    while True:
        # Get user input
        user_input = typer.prompt("You")
        
        # Check for exit commands
        if user_input.lower() in ["quit", "exit", "q"]:
            typer.echo("Goodbye!")
            break
        
        # Add user message to history
        conversation_history.append(HumanMessage(content=user_input))
        
        # Stream the response
        typer.echo("Assistant: ", nl=False)
        full_response = ""
        for chunk in llm.stream(conversation_history):
            content = chunk.content
            print(content, end="", flush=True)
            full_response += content
        print()  # New line after completion
        
        # Add AI response to history
        conversation_history.append(AIMessage(content=full_response))

if __name__ == "__main__":
    app()
