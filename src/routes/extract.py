from fastapi import APIRouter
from application.dtos import ExtractionInfoDTO, DocumentExtractionDTO
from application.services import DocumentExtractionService

router = APIRouter(prefix="/extract")

extraction_service = DocumentExtractionService()

@router.post("")
async def extract(body: ExtractionInfoDTO) -> DocumentExtractionDTO:
    extracted_contents = extraction_service.extract_contents(body.pdf_url, body.case_id)
    document_extraction = extraction_service.save_case_extraction(body.case_id, extracted_contents)
    return document_extraction


__all__ = ["router"]
