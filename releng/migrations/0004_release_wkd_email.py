# Generated by Django 3.2.4 on 2021-06-22 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('releng', '0003_release_pgp_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='release',
            name='wkd_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
