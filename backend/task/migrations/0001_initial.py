# Generated by Django 2.2.20 on 2021-05-26 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0001_initial'),
        ('task_category', '0001_initial'),
        ('task_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField()),
                ('frequency', models.CharField(max_length=7)),
                ('size', models.CharField(max_length=6)),
                ('is_confirmed', models.BooleanField()),
                ('status', models.CharField(max_length=10)),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('timestamp_confirmed', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_category', to='task_category.Category')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_customer', to='task_profile.CustomerProfile')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='task_location', to='location.TaskLocation')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='task_subcategory', to='task_category.Subcategory')),
                ('tasker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_tasker', to='task_profile.TaskerProfile')),
            ],
        ),
        migrations.CreateModel(
            name='TaskTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('timestamp_completed', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('timestamp_started', models.DateTimeField(blank=True, null=True)),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasktransaction_task', to='task.Task')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rating_customer', to='task_profile.CustomerProfile')),
                ('tasker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_tasker', to='task_profile.TaskerProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_customer', to='task_profile.CustomerProfile')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='message_task', to='task.Task')),
                ('tasker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_tasker', to='task_profile.TaskerProfile')),
            ],
        ),
    ]
