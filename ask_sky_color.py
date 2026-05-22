from langchain_lmstudio.llms import LMStudioLLM

def ask_llm(question: str) -> str:
    """
    Connects to the LM Studio LLM server and asks a question.
    """
    model = LMStudioLLM(model="qwen/qwen3-4b-2507", base_url="http://192.168.1.26:1234/v1")
    response = model.invoke(question)
    return response

if __name__ == "__main__":
    answer = ask_llm("what color is the sky?")
    print(answer)