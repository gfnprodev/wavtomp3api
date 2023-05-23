from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import Field

from src.infra.dto.user import UserDTO
from src.infra.schemas.base import BaseSchemaModel

from src.infra.schemas.audiofiles.default import DefaultAudioFileSchema


class DefaultUserSchema(BaseSchemaModel):
    id: int
    token: UUID
    username: str
    audiofiles: list[DefaultAudioFileSchema] = Field(default_factory=list)
    created_at: datetime

    @classmethod
    def from_dto(cls, user: UserDTO):
        return cls(
            id=user.id,
            token=user.token,
            username=user.username,
            audiofiles=list(user.audiofiles),
            created_at=user.created_at
        )
