# Generated by Django 4.2.5 on 2024-01-28 00:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("cardpicker", "0037_tag_parent")]
    operations = [
        migrations.AddField(model_name="tag", name="is_enabled_by_default", field=models.BooleanField(default=True)),
    ]