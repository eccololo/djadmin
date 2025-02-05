# Generated by Django 5.1.5 on 2025-02-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('membership_plan', models.CharField(choices=[('s', 'Standard'), ('p', 'Premium'), ('ux', 'Ultimate Delux')], max_length=2)),
                ('membership_active', models.BooleanField(default=True)),
                ('unique_code', models.CharField(max_length=250)),
            ],
        ),
    ]
