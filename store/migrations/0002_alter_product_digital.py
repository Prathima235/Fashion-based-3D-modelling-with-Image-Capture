# Generated by Django 4.1.2 on 2022-11-03 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='digital',
            field=models.DecimalField(blank=True, decimal_places=2, default=False, max_digits=7, null=True),
        ),
    ]
