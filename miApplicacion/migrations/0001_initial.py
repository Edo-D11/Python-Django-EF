# Generated by Django 5.1.3 on 2024-12-02 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoProducto', models.IntegerField()),
                ('descripcionProductos', models.CharField(max_length=255)),
                ('estatus', models.BooleanField()),
            ],
        ),
    ]
