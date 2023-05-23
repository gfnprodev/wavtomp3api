from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, TYPE_CHECKING
from uuid import UUID

if TYPE_CHECKING:
    from src.infra.dto.user import UserDTO


@dataclass
class AudioFileDTO:
    id: UUID
    user_id: int
    created_at: datetime
    updated_at: datetime
    user: Optional["UserDTO"] = None
