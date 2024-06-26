# Generated by Django 5.0.6 on 2024-06-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0003_medidor_consumo_medidor_lectura_actual_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medidor',
            name='dueño',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='medidor',
            name='fecha_instalacion',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='medidor',
            name='lote',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='medidor',
            name='manzana',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='medidor',
            name='medidor',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
    ]
