from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import SQLAlchemyError
from models import OCRReport
from schemas import OCRReportCreate
from database import async_session


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to restrict origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from typing import AsyncGenerator

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session

@app.get("/")
async def root():
    return {"greeting": "Hello, World!", "message": "Welcome to FastAPI!"}

# POST endpoint to create OCR report
@app.post("/ocr-report/")
async def create_ocr_report(report: OCRReportCreate, session: AsyncSession = Depends(get_session)):
    new_report = OCRReport(**report.dict())
    session.add(new_report)
    try:
        await session.commit()
        await session.refresh(new_report)
        return {"id": new_report.id}
    except SQLAlchemyError as e:
        await session.rollback()
        raise HTTPException(status_code=500, detail=str(e))