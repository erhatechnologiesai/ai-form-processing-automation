import uuid

def process_form_submission(form):
    sub_id = f"SUB-{uuid.uuid4().hex[:6].upper()}"
    sanitized = {}
    for k, v in form.fields.items():
        if isinstance(v, str):
            sanitized[k.strip().lower()] = v.strip()
        else:
            sanitized[k.strip().lower()] = v
            
    return sub_id, "PROCESSED", sanitized, True
