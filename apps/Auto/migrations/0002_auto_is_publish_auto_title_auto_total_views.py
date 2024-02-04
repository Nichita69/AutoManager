# Generated by Django 4.2.9 on 2024-01-20 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='is_publish',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='auto',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='auto',
            name='total_views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]