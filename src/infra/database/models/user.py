import uuid
from typing import TYPE_CHECKING
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.database.models.base import BaseModel, TimestampMixin

if TYPE_CHECKING:
    from src.infra.database.models.audiofile import Audiofile
    from src.infra.dto.audiofile import AudioFileDTO

from src.infra.dto.user import UserDTO


class User(BaseModel, TimestampMixin):
    id: Mapped[int] = mapped_column(sa.INT, primary_key=True, autoincrement=True)
    token: Mapped[UUID] = mapped_column(sa.UUID(as_uuid=True), default=uuid.uuid4)
    username: Mapped[str] = mapped_column(sa.VARCHAR(length=32))
    audiofiles: Mapped[list["Audiofile"]] = relationship(back_populates="user", uselist=True)

    def to_dto(self, audiofiles: list["AudioFileDTO"] | None = None) -> UserDTO:
        if not audiofiles:
            audiofiles = []
        return UserDTO(
            id=self.id,
            token=self.token,
            username=self.username,
            audiofiles=audiofiles,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    def to_dto_audiofiles_prefetched(self) -> UserDTO:
        return self.to_dto(audiofiles=[audiofile.to_dto() for audiofile in self.audiofiles])
