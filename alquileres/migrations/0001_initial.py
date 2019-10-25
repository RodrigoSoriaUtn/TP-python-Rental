# Generated by Django 2.2.6 on 2019-10-25 22:16

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('iata', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('daily_price', models.DecimalField(decimal_places=2, max_digits=13)),
                ('image', models.CharField(max_length=200)),
                ('max_pax', models.IntegerField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquileres.City')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=3)),
                ('created_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='RentalDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquileres.Property')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquileres.Reservation')),
            ],
        ),
    ]