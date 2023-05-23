from uuid import UUID

from src.infra.schemas.base import BaseSchemaModel


class CreateAudioFileSchema(BaseSchemaModel):
    id: UUID
    file_path: str
    user_id: int
