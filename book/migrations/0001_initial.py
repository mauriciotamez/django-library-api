# Generated by Django 3.2 on 2022-05-27 18:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('book_id', models.UUIDField(default=uuid.uuid4)),
                ('genre', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('date_of_publication', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
