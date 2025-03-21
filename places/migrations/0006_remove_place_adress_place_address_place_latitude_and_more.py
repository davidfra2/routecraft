# Generated by Django 5.1.6 on 2025-03-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_remove_place_address_remove_place_latitude_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='adress',
        ),
        migrations.AddField(
            model_name='place',
            name='address',
            field=models.CharField(default='Direccion no especificada', max_length=255),
        ),
        migrations.AddField(
            model_name='place',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='place',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='place',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='places/images/'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='place',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
