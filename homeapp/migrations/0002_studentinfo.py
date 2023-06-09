# Generated by Django 4.2.1 on 2023-05-31 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_fee', models.IntegerField(null=True)),
                ('student_id', models.CharField(max_length=100, null=True)),
                ('student_name', models.CharField(max_length=100, null=True)),
                ('student_date_fee', models.DateField(null=True)),
            ],
            options={
                'db_table': 'studentinfotable',
            },
        ),
    ]
