# Generated by Django 4.2.18 on 2025-03-15 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
