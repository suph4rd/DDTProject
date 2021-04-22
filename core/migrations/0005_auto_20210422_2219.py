# Generated by Django 3.2 on 2021-04-22 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210422_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unioninteres',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.unioninteresprofile', verbose_name='Профиль'),
        ),
        migrations.AlterField(
            model_name='unioninteres',
            name='type',
            field=models.IntegerField(choices=[(0, 'Всего'), (1, 'В сельской местности'), (2, 'По профилям деятельности')], verbose_name='Тип'),
        ),
    ]
