from fastapi import APIRouter
from application.dtos import ExtractInfoDTO, DocummentExtractionDTO

router = APIRouter(prefix="/extract")


@router.post("")
async def extract(body: ExtractInfoDTO) -> dict:
    return {"to": "do"}


__all__ = ["router"]