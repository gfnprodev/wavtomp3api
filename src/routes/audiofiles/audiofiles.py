import logging
import uuid
from uuid import UUID

import fastapi
from fastapi import Depends, UploadFile, File, HTTPException
from starlette.responses import RedirectResponse

from src.common.misc.stub import Stub
from src.common.utilities.audioconverter.converter import convert_audio
from src.common.utilities.minio_client.minio_client import MinioClient
from src.infra.database.dao.holder import HolderDAO
from src.infra.schemas.audiofiles.get import GetRecordDownloadResponseSchema

router = fastapi.APIRouter(prefix='/record', tags=["Record"])
minio_client = MinioClient()
logger = logging.getLogger(__name__)

@router.post(path="/",
             name="Add record",
             response_model=GetRecordDownloadResponseSchema,
             status_code=fastapi.status.HTTP_200_OK)
async def add_record(request: fastapi.Request, user_id: int, token: UUID, file: UploadFile = File(),
                     holder: HolderDAO = Depends(Stub(HolderDAO))):
    user = await holder.user.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.token != token:
        raise HTTPException(status_code=403, detail="Token is invalid")
    if not file.filename.endswith(".wav"):
        raise HTTPException(status_code=400, detail="This file is not WAV")
    new_file_name = uuid.uuid4()
    with open(f"src/common/temp/{new_file_name}.wav", 'wb') as out_file:
        read_file = await file.read()
        out_file.write(read_file)
    await convert_audio(str(new_file_name))
    await minio_client.upload_file(str(new_file_name) + '.mp3', f"src/common/temp/{new_file_name}.mp3", user.username)
    return GetRecordDownloadResponseSchema(url=f"{request.base_url}record?id="
                                               f"{new_file_name}&user_id={user_id}")


@router.get(path="/",
            name="Get record",
            status_code=fastapi.status.HTTP_200_OK)
async def get_record(request: fastapi.Request, id: UUID, user_id: int, holder: HolderDAO = Depends(Stub(HolderDAO))):
    user = await holder.user.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    base_url = str(request.base_url).replace(str(request.base_url.port), "9000")
    url = await minio_client.get_file_url(str(id) + ".mp3", user.username, base_url)
    return RedirectResponse(url)
