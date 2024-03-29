# Generated by Django 3.2.16 on 2022-10-26 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_rename_scroe_job_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='score',
        ),
        migrations.AddField(
            model_name='job',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='url',
            field=models.URLField(max_length=300),
        ),
        migrations.AlterModelTable(
            name='city',
            table='cities',
        ),
        migrations.AlterModelTable(
            name='district',
            table='districts',
        ),
        migrations.AlterModelTable(
            name='job',
            table='job_jobs',
        ),
        migrations.AlterModelTable(
            name='jobposition',
            table='job_job_positions',
        ),
        migrations.AlterModelTable(
            name='workinghour',
            table='job_working_hours',
        ),
        migrations.CreateModel(
            name='benefit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
            ],
            options={
                'db_table': 'job_benefits',
            },
        ),
    ]
