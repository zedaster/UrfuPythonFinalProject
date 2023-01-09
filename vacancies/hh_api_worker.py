from datetime import datetime, timezone, timedelta

import requests
from ciso8601 import parse_datetime
from dateutil.relativedelta import relativedelta

from vacancies.domain_models import Salary, Vacancy


class HhApiWorker:
    def get_vacancies(self, date: datetime, text, count=10, swap_to_workday=True):
        """
        Парсит вакансии с HH.RU в порядке убывания даты
        :param date: нужный день
        :type date: datetime
        :param text: текстовое поле для отбора вакансий
        :type text: str
        :param count: количество вакансии (максимум - 100)
        :type count: int
        :param swap_to_workday: поменять ли указанный день на предыдущий рабочий
        :type swap_to_workday: bool
        :return: Список вакансий
        :rtype: Iterable[Vacancy]
        :raises HhApiWorker.CaptchaException: Если сервер потребовал капчу во время запроса
        """
        # Поменять день если надо
        start_date = datetime(date.year, date.month, date.day, 0, 0, 0, tzinfo=timezone(timedelta(hours=3)))
        if swap_to_workday:
            if date.weekday() == 5:
                start_date -= relativedelta(days=1)
            if date.weekday() == 6:
                start_date -= relativedelta(days=2)

        # Задать лимиты по датам
        end_date = start_date + relativedelta(days=1)

        params = {
            'text': text,
            'specialization': 1,
            'page': 1,
            'per_page': min(count, 100),
            'order_by': 'publication_time',
            'date_from': self._date_to_string(start_date),
            'date_to': self._date_to_string(end_date)
        }
        resp = self._get_from_hh_api('https://api.hh.ru/vacancies', params)
        json = resp.json()
        for item in json['items']:
            v_id = item['id']
            name = item['name']
            employer_name = item['employer']['name']
            area_name = item['area']['name']
            published_at = parse_datetime(item['published_at'])
            salary = None
            if item['salary'] is not None:
                salary_from = item['salary']['from']
                salary_to = item['salary']['to']
                salary_currency = item['salary']['currency']
                salary = Salary(salary_from, salary_to, salary_currency)
            description, skills = self._get_description_and_skills(v_id)
            vacancy = Vacancy(v_id, name, description, skills, employer_name, salary, area_name, published_at)
            yield vacancy

    def _get_description_and_skills(self, vacancy_id):
        resp = self._get_from_hh_api(f'https://api.hh.ru/vacancies/{vacancy_id}')
        json = resp.json()
        return json['description'], list(map(lambda s: s['name'], json['key_skills']))

    class CaptchaException(Exception):
        """
        Ошибка, возникающая при запросе капчи с HH.RU API
        """

        def __init__(self, captcha_url, fallback_url):
            self.captcha_url = captcha_url
            self.fallback_url = fallback_url

    def _get_from_hh_api(self, url, params=None):
        resp = requests.get(url, params)

        # Вернуть ошибку при капче
        if resp.status_code == 403:
            for error in resp.json()['errors']:
                if error['value'] == 'captcha_required':
                    raise self.CaptchaException(error.get("captcha_url", None), error.get("fallback_url", None))

        # Вернуть ошибку при других случаях, когда ответ != 200
        resp.raise_for_status()

        return resp

    @staticmethod
    def _date_to_string(date: datetime):
        """
        Преобразует дату в строку, допустимую для API hh.ru
        :param date: datetime
        :return: str
        """
        return date.strftime('%Y-%m-%dT%H:%M:%S%z')
