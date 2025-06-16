from typing import List, Optional
from sqlalchemy.exc import IntegrityError, DataError
from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.Domain.Models.person import Person
from src.Infrastructure.Repositories.PersonRepository import PersonRepository
from src.Infrastructure.DTO.OperationResultDTO import OperationResultDTO
from src.Infrastructure.DTO.personDTO import PersonDTO
from sqlalchemy.dialects.postgresql import UUID

class PersonService():
    def __init__(self, db: Session):
        self.db = db
        self.repo = PersonRepository(db)

    def get_all(self) -> List[Person]:
        return self.repo.get_person_all()

    def get_by_id(self, person_id: UUID) -> Optional[Person]:
        person = self.repo.get_person_by_id(person_id)
        if not person:
            raise HTTPException(status_code=404, detail="Person not found")
        return person

    def create(self, dto: PersonDTO) -> Optional[Person]:
        try: 
            return self.repo.create_person(dto)
        except IntegrityError as e:
            self.db.rollback()
            raise HTTPException(status_code=409, detail="Person with this email already exists")
        except DataError:
            self.db.rollback()
            raise HTTPException(status_code=400, detail="Field value is too long")

    def update_by_id(self, person_id: UUID, dto: PersonDTO) -> Optional[Person]:
        try:
            updated = self.repo.update_person_by_id(person_id, dto)
            if updated is None:
                raise HTTPException(status_code=404, detail="Person not found")
            return updated
        except IntegrityError as e:
            raise HTTPException(status_code=409, detail="Person with this email already exists")

    def delete_by_id(self, person_id: UUID) -> OperationResultDTO:
        deleted = self.repo.delete_person_by_id(person_id)
        if not deleted:
            raise HTTPException(status_code=404, detail="Person not found") 
        return OperationResultDTO("Person successfully deleted")