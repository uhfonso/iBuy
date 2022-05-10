# Generated by Django 4.0.4 on 2022-05-09 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ibuy', '0008_alter_categoria_tipo_alter_produto_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='produto_fk',
            new_name='produto',
        ),
        migrations.RenameField(
            model_name='comentario',
            old_name='utilizador_fk',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Categoria', to='ibuy.categoria'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.FloatField(default=0),
        ),
    ]