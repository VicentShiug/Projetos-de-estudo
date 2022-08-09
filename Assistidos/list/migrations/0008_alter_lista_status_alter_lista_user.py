# Generated by Django 4.0.6 on 2022-08-09 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('list', '0007_alter_lista_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lista',
            name='status',
            field=models.CharField(choices=[('Assistindo', 'Assistindo'), ('Assistido', 'Assistido'), ('A Assistir', 'A Assistir')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='lista',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
