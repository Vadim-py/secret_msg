# Generated by Django 3.2 on 2021-04-30 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secret', '0002_alter_msg_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='msg',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]