# Generated by Django 4.1.1 on 2022-12-26 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_member_level_member_lft_member_rght_member_tree_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True),
        ),
    ]