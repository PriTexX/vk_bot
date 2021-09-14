from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from . import days_of_the_week
Days = days_of_the_week.Days


class Schedule:
    def __init__(self):
        self.TOKEN = "6b36f9adbed8a5530fcaf91a580e1c94"
        self.GROUP = "211-721"
        self.URL = f"https://rasp.dmami.ru/site/group-html?group={self.GROUP}&token={self.TOKEN}"
        self.week_days = ['Понедельник', 'Вторник', 'Среду', 'Четверг', 'Пятницу', 'Субботу']

    def get_schedule(self, day: Days = None):
        headers = {
            'User-Agent': UserAgent().random
        }
        response = requests.get(self.URL, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        week = soup.find_all('div', class_="schedule-day")

        all_pairs = week[day].find_all('div', class_='pair')
        pairs = []
        for pair in all_pairs:
            if pair.find('div', class_='lessons').text:
                pairs.append(pair)

        SCHEDULE = f"Расписание на {self.week_days[day]}\n\n"
        for pair in pairs:
            auditories = ""
            for auditory in pair.find_all('div', class_='schedule-auditory'):
                auditories+=f"{auditory.text} "

            time = pair.find('div', class_='time').text

            lesson = pair.find('div', class_='bold').text

            teacher = pair.find('div', class_='teacher').text

            text = f"{time}\n\n{auditories}\n{lesson}\n{teacher}\n\n\n"

            SCHEDULE+=text
        return SCHEDULE


