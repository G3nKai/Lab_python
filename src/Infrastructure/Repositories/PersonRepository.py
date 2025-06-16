from sqlalchemy.orm import Session
from typing import List, Optional
from src.Infrastructure.DTO.personDTO import PersonDTO
from src.Domain.Interfaces.IPersonRepository import IPersonRepository
from src.Domain.Models.person import Person
import uuid
from sqlalchemy.dialects.postgresql import UUID

class PersonRepository(IPersonRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_person_all(self) -> List[Person]:
        return self.db.query(Person).all()
    
    def get_person_by_id(self, id: UUID) -> Optional[Person]:
        return self.db.query(Person).filter(Person.id == id).first()
        
    def create_person(self, person_dto: PersonDTO) -> Optional[Person]:
        person = Person(**person_dto.model_dump(exclude_unset=True))
        self.db.add(person)
        self.db.commit()
        self.db.refresh(person)
        return person
    
    def update_person_by_id(self, id: UUID, person_dto: PersonDTO) -> Optional[Person]:
        person = self.db.query(Person).filter(Person.id == id).first()
        if person == None:
            return None
        for key, value in person_dto.model_dump(exclude_unset=True).items():
            setattr(person, key, value)
        self.db.commit()
        self.db.refresh(person)
        return person

    def delete_person_by_id(self, id: UUID) -> bool:
        person = self.db.query(Person).filter(Person.id == id).first()
        if person:
            self.db.delete(person)
            self.db.commit()
            return True
        return False
