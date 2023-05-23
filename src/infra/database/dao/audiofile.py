from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.dao.base import BaseDAO
from src.infra.database.models import Audiofile
from src.infra.dto.audiofile import AudioFileDTO
from src.infra.schemas.audiofiles.get import GetAudioFileSchema


class AudioFileDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def add_audiofile(self, user_id: int, file_path: str) -> AudioFileDTO:
        stmt = insert(Audiofile).values(file_path=file_path, user_id=user_id).returning(Audiofile)

        return (await self._session.scalars(stmt)).first().to_dto()

    async def get_audiofile(self, audiofile: GetAudioFileSchema) -> AudioFileDTO:
        stmt = select(Audiofile).where(Audiofile.user_id == audiofile.user_id, Audiofile.id == audiofile.id)

        result = await self._session.scalars(stmt)

        audiofile: Audiofile = result.first()

        return audiofile.to_dto()
