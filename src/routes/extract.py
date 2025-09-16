from fastapi import APIRouter
from application.dtos import ExtractionInfoDTO, DocumentExtractionDTO
from application.services import DocumentExtractionService

router = APIRouter(prefix="/extract")

extraction_service = DocumentExtractionService()

@router.post("")
async def extract(body: ExtractionInfoDTO) -> DocumentExtractionDTO:
    extracted: DocumentExtractionDTO = extraction_service.extract_contents(
        body.pdf_url, body.case_id)
    return extracted


__all__ = ["router"]