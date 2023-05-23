from pydub import AudioSegment

from src.common.utilities.minio_client.minio_client import MinioClient
import os


async def convert_audio(file_name: str):
    AudioSegment.from_wav(f"src/common/temp/{file_name}.wav").export(f"src/common/temp/{file_name}.mp3", format="mp3")
    os.remove(f"src/common/temp/{file_name}.wav")
