from pydantic import BaseModel


class ExtractionInfoDTO(BaseModel):
    pdf_url: str
    case_id: str


class DocumentTimelineDTO(BaseModel):
    event_id: int
    event_name: str
    event_description: str
    event_date: str
    event_page_init: int
    event_page_end: int
    
    
class DocumentEvidenceDTO(BaseModel):
    evidence_id: int
    evidence_name: str
    evidence_flaw: str | None
    evidence_page_init: int
    evidence_page_end: int


class DocumentExtractionDTO(BaseModel):
    case_id: str
    resume: str
    timeline: list[DocumentTimelineDTO]
    evidence: list[DocumentEvidenceDTO]
    persisted_at: str
