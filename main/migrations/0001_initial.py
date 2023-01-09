# Generated by Django 4.1.5 on 2023-01-09 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemandPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('table', models.TextField(verbose_name='HTML-код таблицы')),
                ('graphic', models.ImageField(upload_to='demand', verbose_name='График')),
            ],
            options={
                'verbose_name': 'Страница "Востребованность"',
                'verbose_name_plural': 'Страница "Востребованность"',
            },
        ),
        migrations.CreateModel(
            name='GeographyPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('general_salary_table', models.TextField(verbose_name='Таблица с зарплатами IT-профессий')),
                ('general_share_table', models.TextField(verbose_name='Таблица с долями по IT-профессиям')),
                ('general_graphic', models.ImageField(upload_to='geography/general', verbose_name='График для IT-профессий')),
                ('prof_subtitle', models.CharField(max_length=128, verbose_name='Подзаголовок для данных по профессии')),
                ('prof_salary_table', models.TextField(verbose_name='Таблица с зарплатами для конкертной профессии')),
                ('prof_share_table', models.TextField(verbose_name='Таблица с долями для конкертной профессии')),
                ('prof_graphic', models.ImageField(upload_to='geography/prof', verbose_name='График для конкертной профессии')),
            ],
            options={
                'verbose_name': 'Страница "География"',
                'verbose_name_plural': 'Страница "География"',
            },
        ),
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='HTML-код')),
            ],
            options={
                'verbose_name': 'Главная Страница',
                'verbose_name_plural': 'Главная Страница',
            },
        ),
        migrations.CreateModel(
            name='HomePageImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Кодовое название')),
                ('image', models.ImageField(upload_to='homepage', verbose_name='Файл')),
            ],
            options={
                'verbose_name': 'Изображение для Главных Страниц',
                'verbose_name_plural': 'Изображения для Главных Страниц',
            },
        ),
        migrations.CreateModel(
            name='SkillPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('graphic', models.ImageField(upload_to='skills', verbose_name='График')),
            ],
            options={
                'verbose_name': 'Страница "Навыки"',
                'verbose_name_plural': 'Страница "Навыки"',
            },
        ),
        migrations.CreateModel(
            name='SkillPageTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('content', models.TextField(verbose_name='HTML-код таблицы')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.skillpage', verbose_name='Страница "Навыки"')),
            ],
            options={
                'verbose_name': 'Таблица на странице "Навыки"',
                'verbose_name_plural': 'Таблицы на странице "Навыки"',
            },
        ),
    ]