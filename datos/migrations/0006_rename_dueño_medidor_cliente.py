# Generated by Django 5.0.6 on 2024-06-02 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datos', '0005_alter_medidor_medidor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medidor',
            old_name='dueño',
            new_name='cliente',
        ),
    ]
