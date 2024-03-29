# Generated by Django 4.2.7 on 2023-12-31 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0006_voters_voting_delete_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='voting',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='voting',
            name='image',
            field=models.ImageField(upload_to='image'),
        ),
    ]
