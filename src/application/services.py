from application.dtos import DocumentExtractionDTO
from domain.repositories import CaseExtractionRepository
from configs.settings import Settings
from google import genai
from google.genai import types

import httpx
import json
import io


prompt = """Dê uma resposta no formato estrito como dado:  
```
{
    "resume": "<aqui coloque um resumo do caso>",
    "timeline": [
        {
            "event_id": <id incremental para cada evento>,
            "event_name": "<nome do evento>",
            "event_description": "<descrição do evento>",
            "event_date": "<data do evento no formato YYYY-MM-DD>",
            "event_page_init": <número da página em que o evento começa a ser mencionado>,
            "event_page_end": <número da última página em que o evento deixa de ser mencionado>
        }
    ],
    "evidence": [
        {
            "evidence_id": <id incremental para cada evidência>,
            "evidence_name": "<nome da evidência>",
            "evidence_flaw": "<falha na lógica da evidência se houver, caso contrário defina null>",
            "evidence_page_init": <número da página em que a evidência começa a ser mencionada>,
            "evidence_page_end": <número da última página em que a evidência deixa de ser mencionada>
        }
    ]
}
```
A resposta não será para olhos humanos, apenas para interpretação de máquina, então mantenha inteiramente
no formato JSON. Os campos timeline e evidence são ambos listas de objetos com as características esperadas
como demonstrado."""


class DocumentExtractionService:
    def __init__(self) -> None:
        self._gemini_client = genai.Client(api_key=Settings.GOOGLE_API_KEY)
        self._case_extraction_repo = CaseExtractionRepository()

    def extract_contents(self, file_url: str, case_id: str) -> object:
        upload_file = self._get_upload_file(file_url)
        response = self._gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[upload_file, prompt],
            config={"response_mime_type": "application/json", "temperature": 0.3,
                    "system_instruction": "Seja preciso e inclua todos os dados relevantes."})
        contents = json.loads(response.text)
        return contents

    def save_case_extraction(self, case_id: str, contents: object | dict) -> DocumentExtractionDTO | None:
        return self._case_extraction_repo.create_case(case_id, json.dumps(contents))

    def _get_upload_file(self, file_url: str) -> io.BytesIO: 
        doc_io = io.BytesIO(httpx.get(file_url).content)
        upload_file = self._gemini_client.files.upload(
            file=doc_io,
            config=dict(mime_type='application/pdf')
        )
        return upload_file
