# Generated by Django 3.2.4 on 2021-06-23 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tipo_cama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tipo_quarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='quarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=200)),
                ('tipo_quarto', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quarto_cama.tipo_quarto')),
            ],
        ),
        migrations.CreateModel(
            name='cama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('l', 'Livre'), ('o', 'Ocupada')], max_length=1)),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=200)),
                ('valor', models.FloatField()),
                ('quarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quarto_cama.quarto')),
                ('tipo_cama', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='quarto_cama.tipo_cama')),
            ],
        ),
    ]
