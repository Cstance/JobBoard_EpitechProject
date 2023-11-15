# Generated by Django 4.2.6 on 2023-10-21 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_alter_advertisements_post_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='advertisement',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='database.advertisements'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='applicant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='message',
            field=models.TextField(default='ewdewfewfefw'),
            preserve_default=False,
        ),
    ]