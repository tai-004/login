# Generated by Django 4.0.8 on 2022-11-29 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0004_alter_subscription_tier'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='subscribed',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='subscriber',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='tier',
        ),
        migrations.RemoveField(
            model_name='tier',
            name='user',
        ),
        migrations.DeleteModel(
            name='PeopleList',
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
        migrations.DeleteModel(
            name='Tier',
        ),
    ]
