from typing import Any

from src.infra.schemas.base import BaseSchemaModel


class CreateUserSchema(BaseSchemaModel):
    username: str

    def for_orm(self, *exclude: Any) -> dict:
        orm_dict = {}
        for key, value in self.dict(exclude=set(exclude)).items():
            if value is not None:
                orm_dict[key] = value
        return orm_dict
