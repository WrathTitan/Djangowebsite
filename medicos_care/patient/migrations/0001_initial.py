# Generated by Django 2.2.4 on 2019-11-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_patient', models.CharField(max_length=100)),
                ('name_of_doctor', models.CharField(max_length=100)),
                ('patient_pescribtion', models.TextField(max_length=500)),
                ('prescribtion_date', models.DateField()),
                ('time_for_medication', models.TimeField()),
            ],
        ),
    ]
