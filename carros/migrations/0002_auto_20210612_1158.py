# Generated by Django 3.1.7 on 2021-06-12 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aceites',
            name='imagen',
            field=models.ImageField(default='', null='True', upload_to='imagen'),
        ),
        migrations.AlterField(
            model_name='baterias',
            name='imagen',
            field=models.ImageField(default='', null='True', upload_to='imagen'),
        ),
        migrations.AlterField(
            model_name='filtros',
            name='imagen',
            field=models.ImageField(default='', null='True', upload_to='imagen'),
        ),
    ]