# Generated by Django 4.2.15 on 2024-08-13 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrinsic',
            name='block_hash',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='extrinsic',
            name='extrinsic_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='extrinsic',
            name='extrinsic_block',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='extrinsic',
            name='extrinsic_hash',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='extrinsic',
            name='extrinsic_idx',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='extrinsic',
            name='extrinsic_netuid',
            field=models.IntegerField(null=True),
        ),
    ]
