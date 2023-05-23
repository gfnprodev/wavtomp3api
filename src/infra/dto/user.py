from dataclasses import dataclass, field
from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from src.infra.dto.audiofile import AudioFileDTO


@dataclass
class UserDTO:
    id: int
    token: UUID
    username: str
    created_at: datetime
    updated_at: datetime
    audiofiles: list["AudioFileDTO"] = field(default_factory=list)
