# Generated by Django 2.2 on 2019-07-21 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190630_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('P', 'Parfüm'), ('KB', 'Kişisel Bakım'), ('OK', 'Oda Kokusu')], max_length=2),
        ),
    ]
