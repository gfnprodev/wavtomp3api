from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.dao.audiofile import AudioFileDAO
from src.infra.database.dao.base import BaseDAO
from src.infra.database.dao.user import UserDAO


class HolderDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)
        self.user = UserDAO(session)
        self.audiofiles = AudioFileDAO(session)
