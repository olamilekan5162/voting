# Generated by Django 4.2.7 on 2023-12-31 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0007_voting_name_alter_voting_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voters',
            name='voted_at',
        ),
        migrations.AddField(
            model_name='voters',
            name='has_voted',
            field=models.BooleanField(default=False),
        ),
    ]