# Generated by Django 4.0.3 on 2022-06-21 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_remove_atributo_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha',
            name='atributos',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.atributo', verbose_name='Atributos'),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='personagem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.personagen', verbose_name='Informações Gerais'),
        ),
    ]
