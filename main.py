from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from core.manager import Manager
from core.logger import logger
import json

manager = Manager()

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("the proses of initialize data started")
    # print("the proses of initialize data started")
    manager.initialize_data()
    logger.info("the proses of initialize data finished")
    # print("the proses of initialize data finished")
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
    uvicorn.run(app, host="127.0.0.1", port=8000)










# manager = Manager()
# manager.initialize_data()
# res = manager.get_all_data()[0]
# print(json.dumps(res, indent=4))