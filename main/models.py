from django.db import models


class Page(models.Model):
    title = models.CharField('Заголовок', max_length=128)

    # def delete(self, **kwargs):
    #     self.active = False
    #     self.save()

    def __str__(self):
        return f'{self._meta.verbose_name} ({self.pk})'

    class Meta:
        abstract = True


class HomePageImage(models.Model):
    name = models.CharField('Кодовое название', max_length=128)
    image = models.ImageField('Файл', upload_to='homepage')

    class Meta:
        verbose_name = 'Изображение для Главных Страниц'
        verbose_name_plural = 'Изображения для Главных Страниц'

    def __str__(self):
        return self.name


class HomePage(Page):
    content = models.TextField('HTML-код')

    class Meta:
        verbose_name = 'Главная Страница'
        verbose_name_plural = 'Главная Страница'


class DemandPage(Page):
    table = models.TextField('HTML-код таблицы')
    graphic = models.ImageField('График', upload_to='demand')

    class Meta:
        verbose_name = 'Страница "Востребованность"'
        verbose_name_plural = 'Страница "Востребованность"'


class GeographyPage(Page):
    general_salary_table = models.TextField('Таблица с зарплатами IT-профессий')
    general_share_table = models.TextField('Таблица с долями по IT-профессиям')
    general_graphic = models.ImageField('График для IT-профессий', upload_to='geography/general')
    prof_subtitle = models.CharField('Подзаголовок для данных по профессии', max_length=128)
    prof_salary_table = models.TextField('Таблица с зарплатами для конкертной профессии')
    prof_share_table = models.TextField('Таблица с долями для конкертной профессии')
    prof_graphic = models.ImageField('График для конкертной профессии', upload_to='geography/prof')

    class Meta:
        verbose_name = 'Страница "География"'
        verbose_name_plural = 'Страница "География"'


class SkillPage(Page):
    graphic = models.ImageField('График', upload_to='skills')

    class Meta:
        verbose_name = 'Страница "Навыки"'
        verbose_name_plural = 'Страница "Навыки"'


class SkillPageTable(models.Model):
    year = models.IntegerField('Год')
    content = models.TextField('HTML-код таблицы')
    page = models.ForeignKey(SkillPage, verbose_name='Страница "Навыки"', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Таблица на странице "Навыки"'
        verbose_name_plural = 'Таблицы на странице "Навыки"'

    def __str__(self):
        return f"{self.year} ({self.page._meta.verbose_name} ({self.page.pk}))"
