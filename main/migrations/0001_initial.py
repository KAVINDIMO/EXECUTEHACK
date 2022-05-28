# Generated by Django 4.0.3 on 2022-05-28 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniqueid', models.CharField(default='0', max_length=100)),
                ('companyname', models.CharField(max_length=100)),
                ('businesstype', models.CharField(max_length=100)),
                ('productname', models.CharField(max_length=100)),
                ('targetaudience', models.CharField(max_length=100)),
                ('theinfo', models.FileField(default='images/default.pdf', upload_to='')),
                ('fileuploaded', models.BooleanField(default=False)),
                ('mail', models.CharField(max_length=1000)),
                ('phno', models.CharField(max_length=100)),
                ('accepted', models.BooleanField(default=False)),
            ],
        ),
    ]
