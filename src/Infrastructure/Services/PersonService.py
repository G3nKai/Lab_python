from typing import List, Optional
from sqlalchemy.orm import Session
from src.Domain.Models.person import Person
from sqlalchemy.orm import Session
from src.Infrastructure.Repositories.PersonRepository import PersonRepository
from src.Infrastructure.DTO.OperationResultDTO import OperationResultDTO
from src.Infrastructure.DTO.personDTO import PersonDTO
import uuid
from sqlalchemy.dialects.postgresql import UUID

class PersonService():
    def __init__(self, db: Session):
        self.repo = PersonRepository(db)

    def get_all(self) -> List[Person]:
        return self.repo.get_person_all()

    def get_by_id(self, person_id: UUID) -> Optional[Person]:
        return self.repo.get_person_by_id(person_id)

    def create(self, dto: PersonDTO) -> Optional[Person]:
        return self.repo.create_person(dto)

    def update_by_id(self, person_id: UUID, dto: PersonDTO) -> Optional[Person]:
        return self.repo.update_person_by_id(person_id, dto)

    def delete_by_id(self, person_id: str) -> Optional[Person]:
        return self.repo.delete_person_by_id(person_id) 