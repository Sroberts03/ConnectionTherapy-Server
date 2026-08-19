import enum
from pydantic import BaseModel

class ConnectionPillarType(str, enum.Enum):
    SPIRITUAL = "spiritual"
    PHYSICAL = "physical"
    SOCIAL = "social"
    INTELLECTUAL = "intellectual"

class ConnectionPillar(BaseModel):
    id: int
    name: ConnectionPillarType
    color: str
    icon: str