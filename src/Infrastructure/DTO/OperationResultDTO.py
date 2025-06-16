from dataclasses import dataclass

@dataclass
class OperationResultDTO:
    status: str
    description: str