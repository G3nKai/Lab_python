from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.Infrastructure.database import sessionLocal
from src.Infrastructure.DTO.personDTO import PersonDTO
from src.Infrastructure.Services.PersonService import PersonService
import uuid

router = APIRouter(prefix="/persons", tags=["Persons"])

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_all_persons(db: Session = Depends(get_db)):
    service = PersonService(db)
    return service.get_all()

@router.get("/{person_id}")
def get_person_by_id(person_id: uuid.UUID, db: Session = Depends(get_db)):
    service = PersonService(db)
    return service.get_by_id(person_id)

@router.post("/")
def create_person(person: PersonDTO, db: Session = Depends(get_db)):
    service = PersonService(db)
    return service.create(person)

@router.put("/{person_id}")
def update_person(person_id: uuid.UUID, person: PersonDTO, db: Session = Depends(get_db)):
    service = PersonService(db)
    return service.update_by_id(person_id, person)


@router.delete("/{person_id}")
def delete_person(person_id: uuid.UUID, db: Session = Depends(get_db)):
    service = PersonService(db)
    return service.delete_by_id(person_id)