from datetime import datetime
from uuid import UUID

from src.infra.schemas.base import BaseSchemaModel


class DefaultAudioFileSchema(BaseSchemaModel):
    id: UUID
    file_path: str
    user_id: int
    created_at: datetime
