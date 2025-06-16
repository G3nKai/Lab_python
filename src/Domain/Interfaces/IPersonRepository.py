from abc import ABC, abstractmethod
from typing import List, Optional
from Domain.Models.person import Person
from Infrastructure.DTO.personDTO import PersonDTO

class IPersonRepository(ABC):
    @abstractmethod
    def get_person_all(self) -> List[Person]:
        pass
    @abstractmethod
    def get_person_by_id(self, id: int) -> Optional[Person]:
        pass
    @abstractmethod
    def delete_person_by_id(self, id: int) -> None:
        pass
    @abstractmethod
    def update_person_by_id(self, id: int, person: PersonDTO) -> Optional[Person]:
        pass
    @abstractmethod
    def create_person(self, person: PersonDTO) -> Person:
        pass