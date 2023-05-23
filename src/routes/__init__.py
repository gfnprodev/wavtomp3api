from fastapi import APIRouter

from src.routes.audiofiles import audiofiles
from src.routes.user import user


def register(root_router: APIRouter) -> None:
    for route in (
        user,
        audiofiles,
    ):
        root_router.include_router(route.router)
