from fastapi import APIRouter
from application.dtos import ExtractionInfoDTO, DocumentExtractionDTO
from application.services import DocumentExtractionService

router = APIRouter(prefix="/extract")

extraction_service = DocumentExtractionService()

@router.post("")
async def extract(body: ExtractionInfoDTO):
    document_extraction = None
    message = "Content not extracted."

    try:
        extracted_contents = extraction_service.extract_contents(body.pdf_url, body.case_id)
        document_extraction = extraction_service.save_case_extraction(body.case_id, extracted_contents)
    except Exception as e:
        message = f"Process couldn't be handled successfuly, exception: {e}"

    if document_extraction is not None:
        data = document_extraction.model_dump_json()
        return data

    return { "message": message }
    

__all__ = ["router"]
