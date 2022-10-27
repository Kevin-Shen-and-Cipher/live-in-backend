# Generated by Django 3.2.16 on 2022-10-23 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=3, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=5, unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.city')),
            ],
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkingHour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('salary', models.PositiveIntegerField()),
                ('tenure', models.PositiveSmallIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('coordinate', models.CharField(max_length=50)),
                ('scroe', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.district')),
                ('job_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.jobposition')),
                ('working_hour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.workinghour')),
            ],
        ),
    ]