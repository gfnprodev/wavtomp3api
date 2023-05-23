from typing import TYPE_CHECKING

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.infra.database.dao.base import BaseDAO
from src.infra.database.models import User
from src.infra.dto.user import UserDTO

if TYPE_CHECKING:
    from src.infra.schemas.user.create import CreateUserSchema


class UserDAO(BaseDAO):
    def __init__(self, session: AsyncSession) -> None:
        super().__init__(session)

    async def add_user(self, user: "CreateUserSchema") -> UserDTO:
        stmt = insert(User).values(user.for_orm()).returning(User)
        return (await self._session.scalars(stmt)).first().to_dto()

    async def get_user(self, user_id: int) -> UserDTO | None:
        stmt = select(User).where(User.id == user_id)

        result = await self._session.scalars(stmt)

        user: User = result.first()

        if not user:
            return None

        return user.to_dto()

    async def get_user_by_username(self, username: str) -> UserDTO | None:
        stmt = select(User).where(User.username == username)

        result = await self._session.scalars(stmt)

        user: User = result.first()
        if not user:
            return None

        return user.to_dto()
