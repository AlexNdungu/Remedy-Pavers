# Generated by Django 3.1.1 on 2021-03-28 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Remedy1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('my_name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('message', models.TextField(blank=True, null=True)),
                ('message_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='upload',
            options={'ordering': ['-upload_time']},
        ),
    ]
