# Generated by Django 3.2.4 on 2021-07-05 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foreignexchange', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foreignexchange',
            name='value',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=8),
        ),
    ]
