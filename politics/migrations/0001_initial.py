# Generated by Django 2.2 on 2018-10-24 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Debate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=10)),
                ('hash', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=20)),
                ('picture', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('side', models.BooleanField()),
                ('username', models.CharField(max_length=20)),
                ('comment', models.CharField(max_length=1000)),
                ('date', models.CharField(max_length=10)),
                ('debate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='politics.Debate')),
            ],
        ),
    ]