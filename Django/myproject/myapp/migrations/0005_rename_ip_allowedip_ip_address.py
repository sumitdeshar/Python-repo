# Generated by Django 4.1.5 on 2023-02-24 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_allowedip_remove_features_ip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allowedip',
            old_name='ip',
            new_name='ip_address',
        ),
    ]
