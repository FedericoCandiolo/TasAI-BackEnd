# Generated by Django 4.2.5 on 2023-09-10 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('nombre_publico', models.CharField(max_length=100)),
            ],
        ),
    ]
