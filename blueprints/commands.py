from vkbottle.bot import Blueprint, Message
from modules import KEYBOARD

bp = Blueprint("commands handler")
bp.labeler.vbml_ignore_case = True


@bp.on.message(text="clear")
async def clear(msg: Message):
    await msg.answer("done", keyboard=None)

