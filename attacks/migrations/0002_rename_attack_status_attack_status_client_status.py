# Generated by Django 4.1.4 on 2022-12-18 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attacks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attack',
            old_name='attack_status',
            new_name='status',
        ),
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.CharField(choices=[('FREE', 'Free'), ('RUNNING', 'Running'), ('DONE', 'Done')], default='FREE', max_length=10),
        ),
    ]
