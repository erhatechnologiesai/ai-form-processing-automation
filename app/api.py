from fastapi import FastAPI
from app.config import settings
from app.models import FormSubmission, FormProcessingResult
from app.services.form_validator import process_form_submission

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/submit-form", response_model=FormProcessingResult)
def submit(form: FormSubmission):
    sub_id, status, fields, notified = process_form_submission(form)
    return FormProcessingResult(
        submission_id=sub_id,
        status=status,
        sanitized_fields=fields,
        notification_dispatched=notified
    )
