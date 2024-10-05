# Generated by Django 5.1.1 on 2024-10-05 09:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kittens_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='name',
            field=models.CharField(choices=[('persian', 'Персидская'), ('maine_coon', 'Мейн-кун'), ('siberian', 'Сибирская'), ('british_shorthair', 'Британская короткошерстная'), ('ragdoll', 'Рэгдолл'), ('other', 'Другая')], max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='kitten',
            name='age',
            field=models.PositiveIntegerField(help_text='Укажите возраст котенка в месяцах.'),
        ),
        migrations.AlterField(
            model_name='kitten',
            name='color',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='KittenRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('kitten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='kittens_app.kitten')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('kitten', 'user')},
            },
        ),
    ]
