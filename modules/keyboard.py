from vkbottle import Keyboard, KeyboardButtonColor, Callback
from . import days_of_the_week

Days = days_of_the_week.Days
KEYBOARD_SCHEDULE = (
        Keyboard(one_time=True)
        .add(Callback("Понедельник", {"cmd": "get_schedule", "day": Days.MONDAY.value}), color=KeyboardButtonColor.PRIMARY)
        .add(Callback("Вторник", {"cmd": "get_schedule", "day": Days.TUESDAY.value}), color=KeyboardButtonColor.PRIMARY)
        .add(Callback("Среда", {"cmd": "get_schedule", "day": Days.WEDNESDAY.value}), color=KeyboardButtonColor.PRIMARY)
        .row()
        .add(Callback("Четверг", {"cmd": "get_schedule", "day": Days.THURSDAY.value}), color=KeyboardButtonColor.PRIMARY)
        .add(Callback("Пятница", {"cmd": "get_schedule", "day": Days.FRIDAY.value}), color=KeyboardButtonColor.PRIMARY)
        .add(Callback("Суббота", {"cmd": "get_schedule", "day": Days.SATURDAY.value}), color=KeyboardButtonColor.PRIMARY)
        .get_json()
)
