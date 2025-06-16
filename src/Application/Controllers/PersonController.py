from sqlalchemy.exc import IntegrityError
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from src.Infrastructure.database import sessionLocal
from src.Infrastructure.DTO.personDTO import PersonDTO
from src.Infrastructure.Services.PersonService import PersonService
from src.Infrastructure.DTO.OperationResultDTO import OperationResultDTO
import uuid

router = APIRouter(prefix="/persons", tags=["Persons"])

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")#+
def get_all_persons(db: Session = Depends(get_db)):
    service = PersonService(db)
    return service.get_all()

@router.get("/{person_id}")#+
def get_person_by_id(person_id: uuid.UUID, db: Session = Depends(get_db)):
    service = PersonService(db)
    person = service.get_by_id(person_id)
    if not person:
        raise HTTPException(status_code=404, detail="Person not found")
    return person

@router.post("/")#
def create_person(person: PersonDTO, db: Session = Depends(get_db)):
    service = PersonService(db)
    try:
        return service.create(person)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=409, detail="Person with this email already exists")

@router.put("/{person_id}")
def update_person(person_id: uuid.UUID, person: PersonDTO, db: Session = Depends(get_db)):
    service = PersonService(db)
    updated = service.update_by_id(person_id, person)
    if not updated:
        raise HTTPException(status_code=404, detail="Person not found")
    return updated

@router.delete("/{person_id}")
def delete_person(person_id: uuid.UUID, db: Session = Depends(get_db)):
    service = PersonService(db)
    return service.delete_by_id(person_id)