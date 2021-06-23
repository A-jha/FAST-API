# FastApi

## What is FastApi ?

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

## Why should i use it ?

- Fast : Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
- Fast to code
- Fewer Bugs
- Intuitive : Less time debugging
- Easy : Design to use easily
- Short : Minizes code redundancy .
- Robust : Get production ready code with interactive documentation.
- Standards-Based

## How to install FastAPI

- install fastAPI

```bash
pip install fastapi
```

- Install uvicorn it provides auto reload features and You will also need an ASGI server, for production such as Uvicorn.

```bash
pip install uvicorn
```

## What is endpoint?

An API endpoint is the entry point to the commmunication channel when two system are interacting.

- It refers to touch point of the communication between API and server.

## Create an endpoint and return a dictionary

```python
from fastapi import FastAPI

# create an api object
app = FastAPI()

# create endpoint
@app.get("/")
def home():
    return {"Name": "Avinash jha"}

@app.get("/hi")
def hi():
    return{"greet": "hi guys"}
```

## How to run the server ?

```bash
uvicort finename:app --reload
```

## Lets Test it

- Now if we go to http://127.0.0.1:8000/ then we will find a json output

  ```json
  {
    "Name": "Avinash jha"
  }
  ```

- if we go to http://127.0.0.1:8000/hi then the output is

  ```json
  {
    "greet": "hi guys"
  }
  ```
