# Generated by Django 2.0.6 on 2018-06-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Codedjob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_text', models.TextField()),
                ('submit_time', models.DateTimeField()),
            ],
        ),
    ]
