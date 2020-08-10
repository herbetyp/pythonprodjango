# Generated by Django 3.0.8 on 2020-08-01 18:22
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0002_populando_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False, verbose_name='order')),
                ('titulo', models.CharField(max_length=64)),
                ('slug', models.SlugField(unique=True)),
                ('modulo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='modulos.Modulo')),
            ],
            options={'ordering': ('order',), 'abstract': False,},
        ),
    ]