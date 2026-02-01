# Working with Local LLMS
This repo is just for education purposes. It's meant to get to you started by working with local llms.

# Getting Started 
## Prerequisites
- Ollama installed and running
- Python 3.13 or higher

## Creating the Environment
First create your environment
```
conda env create -f environment.yml
```
If your conda in not up to date, or giving you trouble try uv: 

Activate your environment
```
conda activate local-llms
```

Download the model
```
ollama pull llama3.1:8b
```

Run the example
```
python chat_with_llama.py
```


### Using uv instead of conda
If you prefer to use uv instead of conda, you can install it and use it to create your environment:
```
uv sync
```

Activate env (for windows)
```
.\.venv\Scripts\activate.ps1
```

For linux/mac
```
source .venv/bin/activate
```
