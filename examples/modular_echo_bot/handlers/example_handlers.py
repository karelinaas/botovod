# Пусть мы создали фильтр KnownUser.
# Чтобы не вешать его на каждый хэндлер, можно закрепить его за роутером.


# router.message.filter(KnownUser())
#
#
# @router.message(filter_1, filter_2)
# async def handler_1(message: Message):
#     # ...
#
#
# @router.message(filter_3)
# async def handler_2(message: Message):
#     # ...
#
#
# @router.message(filter_4, filter_5)
# async def handler_3(message: Message):
#     # ...
#
#
# @router.message(filter_6)
# async def handler_4(message: Message):
#     # ...
