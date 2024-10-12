# Generated by Django 4.2.16 on 2024-10-12 09:31

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sith',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('is_shadow_hand', models.BooleanField(default=False, verbose_name='Рука Тени')),
                ('answers', models.CharField(default='', max_length=3, verbose_name='Ответы')),
                ('master', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shadow_hands', to='sith_app.sith', verbose_name='Мастер')),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.planet', verbose_name='Планета, на которой обучает')),
                ('question_set', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.questionset', verbose_name='Тестовое испытание')),
            ],
            options={
                'verbose_name': 'Ситх',
                'verbose_name_plural': 'Ситхи',
            },
            bases=('main_app.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
