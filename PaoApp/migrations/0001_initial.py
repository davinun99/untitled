# Generated by Django 2.2.11 on 2020-03-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('nombre_real', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
