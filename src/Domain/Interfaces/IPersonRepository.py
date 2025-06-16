from abc import ABC, abstractmethod
from typing import List, Optional
from Infrastructure.DTO.OperationResultDTO import OperationResultDTO
from src.Domain.Models.person import Person
from src.Infrastructure.DTO.personDTO import PersonDTO
from sqlalchemy.dialects.postgresql import UUID
import uuid

class IPersonRepository(ABC):
    @abstractmethod
    def get_person_all(self) -> List[Person]:
        pass
    @abstractmethod
    def get_person_by_id(self, id: UUID) -> Optional[Person]:
        pass
    @abstractmethod
    def delete_person_by_id(self, id: UUID) -> bool:
        pass
    @abstractmethod
    def update_person_by_id(self, id: UUID, person: PersonDTO) -> Optional[Person]:
        pass
    @abstractmethod
    def create_person(self, person: PersonDTO) -> Optional[Person]:
        pass