# Generated by Django 3.2 on 2022-05-27 09:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookcase', '0025_alter_rack_rack_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rack',
            name='rack_id',
            field=models.UUIDField(default=uuid.UUID('6f695292-2e8d-44e7-87d7-59f0afa89c4c')),
        ),
    ]
