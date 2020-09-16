# Generated by Django 3.1.1 on 2020-09-16 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='email',
        ),
        migrations.AlterField(
            model_name='employee',
            name='phoneNumber',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='state',
            field=models.CharField(choices=[('', 'Choose...'), ('NY', 'New York'), ('CA', 'California'), ('TX', 'Texas')], default='1', max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='zipCode',
            field=models.BigIntegerField(),
        ),
    ]
