# Generated by Django 3.2 on 2022-05-25 02:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bookcase', '0018_auto_20220525_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitem',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0d73bd0f-5d11-4b7e-9b22-b01c76539092'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rack',
            name='rack_id',
            field=models.UUIDField(default=uuid.UUID('5095e4f4-b821-4101-a779-713e5f3a5c78')),
        ),
    ]
