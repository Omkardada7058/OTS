# Generated by Django 4.2.5 on 2023-10-07 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTS', '0003_question_ans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='ans',
            field=models.CharField(max_length=2),
        ),
    ]