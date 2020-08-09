# Generated by Django 2.2.13 on 2020-08-09 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registro_paciente', '0002_auto_20200729_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('id_sexo', models.AutoField(primary_key=True, serialize=False)),
                ('sexo', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'sexo',
            },
        ),
        migrations.AddField(
            model_name='paciente',
            name='id_sexo',
            field=models.ForeignKey(db_column='id_sexo', default='', on_delete=django.db.models.deletion.DO_NOTHING, to='registro_paciente.Sexo'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='paciente',
            unique_together={('id_paciente', 'id_localidad', 'id_congregacion', 'id_estado_civil', 'id_referencia', 'id_sexo')},
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='sexo',
        ),
    ]
