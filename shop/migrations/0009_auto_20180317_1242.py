# Generated by Django 2.0.2 on 2018-03-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_productclass_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='nophoto.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='image',
            field=models.ImageField(blank=True, default='nophoto.png', upload_to=''),
        ),
    ]
