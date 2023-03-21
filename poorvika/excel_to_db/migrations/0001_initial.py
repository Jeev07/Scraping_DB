# Generated by Django 4.1.7 on 2023-03-17 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kitchen_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_ID', models.IntegerField(default='')),
                ('Item_Code', models.IntegerField(default='')),
                ('Model_Name', models.CharField(default='', max_length=100)),
                ('Poorvika_Price', models.IntegerField(default='')),
                ('Flipkart_Price', models.IntegerField(default='')),
                ('Amazon_Price', models.IntegerField(default='')),
                ('Croma_price', models.IntegerField(default='')),
                ('Vijay_Price', models.IntegerField(default='')),
                ('Reliance_Price', models.IntegerField(default='')),
            ],
        ),
    ]
