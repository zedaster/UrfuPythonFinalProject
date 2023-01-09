from django.db import models

from main.models import Page


class VacanciesPage(Page):
    date = models.DateField('День выгрузки')
    search_query = models.CharField('Поисковой запрос для API hh.ru', max_length=256)
    count = models.IntegerField('Количество вакансий')

    class Meta:
        verbose_name = 'Страница "Вакансии"'
        verbose_name_plural = 'Страница "Вакансии"'
