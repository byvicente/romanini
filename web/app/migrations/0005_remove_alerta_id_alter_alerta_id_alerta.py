# Generated by Django 4.1.1 on 2023-01-07 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_solicitud_id_alter_solicitud_id_solicitud'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alerta',
            name='id',
        ),
        migrations.AlterField(
            model_name='alerta',
            name='id_alerta',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]