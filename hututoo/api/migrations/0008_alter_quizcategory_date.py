# Generated by Django 4.0.2 on 2022-03-07 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_transaction_points_method_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizcategory',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]