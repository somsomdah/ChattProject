# Generated by Django 3.0.8 on 2021-01-08 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210108_1817'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointment',
            options={'ordering': ['date', 'time']},
        ),
        migrations.AlterModelOptions(
            name='coursedetail',
            options={'ordering': ['course__id', 'index']},
        ),
        migrations.AlterOrderWithRespectTo(
            name='course',
            order_with_respect_to='teacher',
        ),
        migrations.AlterOrderWithRespectTo(
            name='coursetime',
            order_with_respect_to='course',
        ),
        migrations.AlterOrderWithRespectTo(
            name='enrollment',
            order_with_respect_to='user',
        ),
        migrations.AlterOrderWithRespectTo(
            name='record',
            order_with_respect_to='enrollment',
        ),
        migrations.AlterOrderWithRespectTo(
            name='relatedlocation',
            order_with_respect_to='teacher',
        ),
    ]
