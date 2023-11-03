from aiogram.filters import BaseFilter
from aiogram.types import Message


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[int | str]) -> None:
        self.admin_ids = [int(_id) for _id in admin_ids]

    async def __call__(self, message: Message) -> bool:
        return message.from_user.id in self.admin_ids
