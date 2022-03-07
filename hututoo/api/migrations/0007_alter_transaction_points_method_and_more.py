# Generated by Django 4.0.2 on 2022-03-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_transaction_points_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='points_method',
            field=models.CharField(blank=True, choices=[('SignUp Bonus', 'SignUp Bonus'), ('Referral Bonus', 'Referral Bonus'), ('Events Points', 'Events Points')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='points_status',
            field=models.CharField(blank=True, choices=[('Credit', 'Credit'), ('Debit', 'Debit')], max_length=50, null=True),
        ),
    ]