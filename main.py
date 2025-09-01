from core.manager import Manager
from core.logger import logger
from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn

manager = Manager()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("the proses of initialize data started")
    manager.initialize_data()
    logger.info("the proses of initialize data finished")
    yield
    print("the Enricher server finished")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def health():
    return {"health": "ok"}

@app.get("/antisemitic_documents")
def get_antisemitic_documents():
    respo = manager.get_all_data()
    return respo or {"msg": "there is nothing to show"}

@app.get("/antisemitic_documents/weapons")
def get_antisemitic_documents_with_weapons():
    respo = manager.get_all_data_more_weapons()
    return respo or {"msg": "there is nothing to show"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)