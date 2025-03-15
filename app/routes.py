from fastapi import APIRouter, Query
from .database import collection
from .models import Document
from typing import List, Optional

router = APIRouter()

@router.post("/documents/")
def add_document(doc: Document):
    doc_dict = doc.dict()
    result = collection.insert_one(doc_dict)
    return {"id": str(result.inserted_id)}

@router.get("/documents/", response_model=List[Document])
def get_documents(category: Optional[str] = Query(None)):
    query = {"category": category} if category else {}
    documents = list(collection.find(query, {"_id": 0}))
    return documents
