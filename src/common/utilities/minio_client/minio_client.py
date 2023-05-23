import os
from typing import Any

from fastapi import HTTPException
from miniopy_async import Minio, S3Error
import logging

from pydub import AudioSegment

logger = logging.getLogger(__name__)


class MinioClient:
    def __init__(self):
        self.client: Minio = Minio("minio:9000",
                                   access_key="minio",
                                   secret_key="Sdffas422",
                                   secure=False)

    async def upload_file(self, file_name: str, file_path: str, username: str) -> None:
        await self.client.fput_object(username, file_name, file_path)
        os.remove(file_path)

    async def create_user_bucket(self, username: str) -> None:
        bucket = await self.client.bucket_exists(username)
        if not bucket:
            await self.client.make_bucket(username)

    async def get_file_url(self, file_name: str, username: str, base_url_host: str) -> Any:
        try:
            url = await self.client.presigned_get_object(username, file_name, change_host=base_url_host)
        except S3Error as e:
            raise HTTPException(status_code=404, detail=str(e))
        return url

    async def get_file(self, file_name: str, user_id: int) -> None:
        try:
            await self.client.fget_object(str(user_id), file_name, f"src/common/temp/{file_name}")
        except Exception as e:
            logger.exception(e)
            raise e
