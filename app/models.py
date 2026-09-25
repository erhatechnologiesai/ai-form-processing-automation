from pydantic import BaseModel
from typing import Dict, Any, Optional

class FormSubmission(BaseModel):
    form_id: str
    submitter_name: str
    submitter_email: str
    fields: Dict[str, Any]

class FormProcessingResult(BaseModel):
    submission_id: str
    status: str # PROCESSED, VALIDATION_ERROR
    sanitized_fields: Dict[str, Any]
    notification_dispatched: bool
