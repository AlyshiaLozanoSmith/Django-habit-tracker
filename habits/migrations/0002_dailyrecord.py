# Generated by Django 3.0.6 on 2020-06-05 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(blank=True, null=True)),
                ('recorded_on', models.DateField(blank=True, null=True)),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dailyrecord', to='habits.Habit')),
            ],
        ),
    ]
