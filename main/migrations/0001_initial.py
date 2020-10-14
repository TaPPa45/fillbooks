# Generated by Django 2.2.12 on 2020-10-14 00:19

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя клиента')),
                ('phone_number', models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message='Номер телефона должен быть указан в формате +71234567890', regex='^\\+?1?\\d{9,15}$')])),
            ],
            options={
                'verbose_name_plural': 'Список клиентов',
                'verbose_name': 'Клиент',
            },
        ),
        migrations.CreateModel(
            name='GoodsBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Производитель')),
            ],
            options={
                'verbose_name_plural': 'Список производтелей',
                'verbose_name': 'Прозводитель',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Характеристка')),
            ],
            options={
                'verbose_name_plural': 'Список характеристик',
                'verbose_name': 'Характеристика',
            },
        ),
        migrations.CreateModel(
            name='PropertyValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=50, unique=True, verbose_name='Значение характеристики')),
            ],
            options={
                'verbose_name_plural': 'Список значений характеристик',
                'verbose_name': 'Значение характеристики',
            },
        ),
        migrations.CreateModel(
            name='PropertyBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Блок характеристик')),
                ('properties', models.ManyToManyField(to='main.Property', verbose_name='Характеристики')),
            ],
            options={
                'verbose_name_plural': 'Список блоков характеристик',
                'verbose_name': 'Блок характеристик',
            },
        ),
        migrations.AddField(
            model_name='property',
            name='value',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.PropertyValue'),
        ),
        migrations.CreateModel(
            name='GoodsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Модель')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.GoodsBrand')),
            ],
            options={
                'verbose_name_plural': 'Список моделей',
                'verbose_name': 'Модель',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('good_id', models.CharField(max_length=16, unique=True, verbose_name='ID товара')),
                ('branch', models.CharField(max_length=50, verbose_name='Филиал')),
                ('price', models.CharField(blank=True, default='', max_length=10, verbose_name='Цена')),
                ('status', models.CharField(choices=[('Ожидает оценки', 'Ожидает оценки'), ('Отказ', 'Отказ'), ('Преобретен', 'Преобретен'), ('Оценен', 'Оценен')], default='Ожидает оценки', max_length=20, verbose_name='Статус')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.GoodsBrand', verbose_name='Производитель')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Customers', verbose_name='Клиент')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.GoodsModel', verbose_name='Модель')),
                ('property_block', models.ManyToManyField(to='main.PropertyBlock', verbose_name='Блоки характеристик')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Добавивший пользователь')),
            ],
            options={
                'verbose_name_plural': 'Список товаров',
                'verbose_name': 'Товар',
            },
        ),
    ]