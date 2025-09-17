from infrastructure.psql_client import PSQLClient
from application.dtos import DocumentExtractionDTO

import json


class CaseExtractionRepository:
    def __init__(self):
        self._db_client = PSQLClient.get_instance()
    
    def create_case(self, case_id: str, contents: str) -> DocumentExtractionDTO | None:
        success = self._db_client.exec(
            "INSERT INTO document_extractions (case_id, contents) "
            " VALUES (%(case_id)s, %(contents)s)",
            {"case_id": case_id, "contents": contents})

        if success:
            query_result = self._db_client.query(
                "SELECT (id, case_id, contents, persisted_at) FROM document_extractions "
                " WHERE case_id = %(case_id)s ORDER BY persisted_at DESC;",
                {"case_id": case_id})
            if len(query_result) > 0:
                case_data = query_result[0][0]
                case_id = case_data[1]
                contents = json.loads(case_data[2])
                persisted_at = case_data[3]
                return DocumentExtractionDTO(
                    case_id=case_id,
                    persisted_at=persisted_at,
                    **contents
                )

        return None
    
    def get_caset(self, case_id) -> DocumentExtractionDTO | None:
        pass # TODO

        