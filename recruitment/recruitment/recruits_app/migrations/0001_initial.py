# Generated by Django 4.2.16 on 2024-10-12 14:11

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
            name='Recruit',
            fields=[
                ('customuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.planet', verbose_name='Planet')),
                ('question_set', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.questionset', verbose_name='Test Task')),
            ],
            options={
                'verbose_name': 'Recruit',
                'verbose_name_plural': 'Recruits',
            },
            bases=('main_app.customuser',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
