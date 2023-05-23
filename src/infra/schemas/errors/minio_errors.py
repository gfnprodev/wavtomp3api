from src.infra.database.models.base import BaseModel


class FileNotFounded(BaseModel):
    messae: str = "File Not founded"
