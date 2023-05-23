import uuid
from typing import TYPE_CHECKING
from uuid import UUID

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infra.database.models.base import BaseModel, TimestampMixin
from src.infra.dto.audiofile import AudioFileDTO
from src.infra.dto.user import UserDTO

if TYPE_CHECKING:
    from src.infra.database.models.user import User


class Audiofile(BaseModel, TimestampMixin):
    id: Mapped[UUID] = mapped_column(sa.UUID(as_uuid=True), primary_key=True)
    user_id: Mapped[UUID] = mapped_column(sa.ForeignKey("users.id", ondelete='CASCADE'))
    user: Mapped["User"] = relationship(back_populates='audiofiles')

    def to_dto(self, user: UserDTO | None = None) -> AudioFileDTO:
        return AudioFileDTO(
            id=self.id,
            user_id=self.user_id,
            user=user,
            created_at=self.created_at,
            updated_at=self.updated_at
        )

    def to_dto_user_prefetched(self) -> AudioFileDTO:
        return self.to_dto(self.user.to_dto())
