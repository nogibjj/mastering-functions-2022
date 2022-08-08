from fastapi import FastAPI
import uvicorn
from nlplogic.corenlp import get_phrases

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello NLP"}


@app.get("/wikiphrases/{name}")
async def wikiphrase(name: str):
    """Generates NLP noun phrases from wikipedia name"""

    print(f"Passed in {name}")
    noun_phrases = get_phrases(name)
    return {"noun_phrases": noun_phrases}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
