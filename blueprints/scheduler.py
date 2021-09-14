from vkbottle.bot import Blueprint, Message
from vkbottle import GroupEventType, GroupTypes, VKAPIError, EMPTY_KEYBOARD
from vkbottle.modules import json
from modules import KEYBOARD
from time import time
from modules import Schedule

bp = Blueprint("schedule handler")
bp.labeler.vbml_ignore_case = True


@bp.on.message(text="расписание")
async def schedule(msg: Message):
    keyboard = KEYBOARD
    await msg.answer("&#13;", keyboard=keyboard)


@bp.on.raw_event(GroupEventType.MESSAGE_EVENT, dataclass=GroupTypes.MessageEvent)
async def message_event_handler(event: GroupTypes.MessageEvent):
    if event.object.payload["cmd"] == "get_schedule":
        sch = Schedule().get_schedule(event.object.payload["day"])
        await bp.api.messages.send(
            event_id=event.object.event_id,
            peer_id=event.object.peer_id,
            user_id=event.object.user_id,
            random_id=time(),
            keyboard=EMPTY_KEYBOARD,
            message=sch,
        )

