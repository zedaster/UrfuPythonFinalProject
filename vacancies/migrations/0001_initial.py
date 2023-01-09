# Generated by Django 4.1.5 on 2023-01-09 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VacanciesPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('date', models.DateField(verbose_name='День выгрузки')),
                ('search_query', models.CharField(max_length=256, verbose_name='Поисковой запрос для API hh.ru')),
                ('count', models.IntegerField(verbose_name='Количество вакансий')),
            ],
            options={
                'verbose_name': 'Страница "Вакансии"',
                'verbose_name_plural': 'Страница "Вакансии"',
            },
        ),
    ]