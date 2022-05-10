# Generated by Django 4.0.4 on 2022-05-10 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_docter_password2_remove_docter_patient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='docter',
            name='salary',
        ),
        migrations.AlterField(
            model_name='docter',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL),
        ),
    ]