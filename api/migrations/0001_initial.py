# Generated by Django 4.2.4 on 2023-10-24 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('photo', models.ImageField(blank=True, upload_to='candidates')),
                ('bio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=11)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('is_open', models.BooleanField(default=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('max_vote', models.IntegerField()),
                ('priority', models.IntegerField()),
                ('election', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.election')),
            ],
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('SuperAdmin', 'SuperAdmin'), ('Admin', 'Admin'), ('Voter', 'Voter')], default='Voter', max_length=10)),
                ('verified', models.BooleanField(default=True)),
                ('voted', models.BooleanField(default=False)),
                ('election', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.election')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.candidate')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.election')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.position')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.voter')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.election'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.position'),
        ),
    ]