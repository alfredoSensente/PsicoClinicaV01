# Generated by Django 4.1.5 on 2023-03-02 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='clinic_role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='users.clinicrole'),
            preserve_default=False,
        ),
    ]
