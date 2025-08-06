from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.qa_service import qa_system_instance

router = APIRouter()

class QuestionRequest(BaseModel):
    question: str

class AnswerResponse(BaseModel):
    answer: str

@router.post("/ask", response_model=AnswerResponse)
def ask_question(data: QuestionRequest):
    if not data.question.strip():
        raise HTTPException(status_code=400, detail="Pergunta não pode estar vazia.")
    
    answer = qa_system_instance.ask(data.question)
    return {"answer": answer}
