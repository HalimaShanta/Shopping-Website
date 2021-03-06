# Generated by Django 3.0.8 on 2021-09-04 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20210904_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourite',
            name='complete',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='favourite',
            name='fav_date',
        ),
        migrations.AddField(
            model_name='favourite',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Home'),
        ),
        migrations.AddField(
            model_name='favourite',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Customer'),
        ),
        migrations.DeleteModel(
            name='FavoriteItem',
        ),
    ]
