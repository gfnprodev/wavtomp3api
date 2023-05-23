from uuid import UUID

from src.infra.schemas.base import BaseSchemaModel


class GetAudioFileSchema(BaseSchemaModel):
    id: UUID
    user_id: int


class GetRecordDownloadResponseSchema(BaseSchemaModel):
    url: str
