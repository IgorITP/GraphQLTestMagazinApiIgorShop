# Generated by Django 3.1 on 2021-10-27 10:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100, verbose_name='Login')),
                ('password', models.CharField(default='', max_length=100, verbose_name='Password')),
                ('email', models.EmailField(default='', max_length=100, verbose_name='Email')),
                ('first_name', models.CharField(default='', max_length=100, verbose_name='Name')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Registration Data')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Products', to='api.category'),
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(default='', max_length=100, verbose_name='Product')),
                ('quantity', models.CharField(default='', max_length=100, verbose_name='Quantity')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.users', verbose_name='Users')),
            ],
        ),
    ]
