# Generated by Django 2.0.6 on 2018-06-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0007_codedjob_gender_words'),
    ]

    operations = [
        migrations.RenameField(
            model_name='codedjob',
            old_name='gender_words',
            new_name='fem_words',
        ),
        migrations.AddField(
            model_name='codedjob',
            name='masc_words',
            field=models.TextField(default=''),
        ),
    ]
