from fastapi import APIRouter
from ..models.users import User
from ..models.pydantic_users import UserCheck


user_router = APIRouter(prefix="/users")


@user_router.get("/{uid}")
async def get_user(uid: int):
    user = await User.get_or_404(uid)
    return user.to_dict()


@user_router.post("")
async def add_user(user: UserCheck):
    rv = await User.create(nickname=user.nickname)
    return rv.to_dict()


@user_router.delete("/{uid}")
async def delete_user(uid: int):
    user = await User.get_or_404(uid)
    await user.delete()
    return dict(id=uid)


def init_app(app):
    app.include_router(user_router)
