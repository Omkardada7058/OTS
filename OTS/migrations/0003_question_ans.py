# Generated by Django 4.2.5 on 2023-10-06 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OTS', '0002_alter_candidate_points_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='ans',
            field=models.CharField(default='a', max_length=5),
        ),
    ]