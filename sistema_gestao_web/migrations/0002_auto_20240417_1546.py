# Generated by Django 3.2.5 on 2024-04-17 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema_gestao_web', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='data_leitura',
        ),
        migrations.AddField(
            model_name='livro',
            name='finalizado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='livro',
            name='titulo',
            field=models.TextField(max_length=50),
        ),
    ]
