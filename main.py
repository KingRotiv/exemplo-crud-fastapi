import uvicorn
from fastapi import FastAPI

import texts
from api import router as api_router
from _site import router as site_router


app = FastAPI(
    title=texts.title,
    description=texts.description,
)
app.include_router(api_router, prefix="/api")
app.include_router(site_router)


# Iniciando uvicorn
if __name__ == "__main__":
    uvicorn.run(app=app)
