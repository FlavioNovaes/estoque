# Generated by Django 4.1.7 on 2023-06-06 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_alter_cores_options'),
        ('entrada', '0002_alter_entradas_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entradas',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.produtos', verbose_name='Produto'),
        ),
    ]
