import fastapi
from fastapi import Depends, HTTPException

from src.common.misc.stub import Stub
from src.infra.database.dao.holder import HolderDAO
from src.infra.schemas.user.create import CreateUserSchema
from src.infra.schemas.user.default import DefaultUserSchema
from src.routes.audiofiles.audiofiles import minio_client

router = fastapi.APIRouter(prefix='/user', tags=["User"])


@router.post(path="/",
             name="Add user",
             response_model=DefaultUserSchema,
             status_code=fastapi.status.HTTP_200_OK)
async def add_user(user: CreateUserSchema, holder: HolderDAO = Depends(Stub(HolderDAO))):
    user_exists = await holder.user.get_user_by_username(user.username)
    if user_exists:
        raise HTTPException(status_code=418, detail="User already registered")
    new_user = await holder.user.add_user(user)
    await holder.commit()
    await minio_client.create_user_bucket(new_user.username)
    return DefaultUserSchema.from_dto(new_user)
