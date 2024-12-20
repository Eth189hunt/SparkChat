# Generated by Django 4.1.5 on 2024-11-12 03:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_server_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="directmessage",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="friendrequest",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="server",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="textchannelmessage",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
