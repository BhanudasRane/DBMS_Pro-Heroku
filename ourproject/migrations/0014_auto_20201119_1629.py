# Generated by Django 3.1.2 on 2020-11-19 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourproject', '0013_auto_20201119_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell_product',
            name='book_type',
            field=models.CharField(choices=[('Second-Hand', 'Second-Hand'), ('Original', 'Original')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='sell_product',
            name='branch',
            field=models.CharField(choices=[('Computer Engineer', 'Computer Engineer'), ('Mechanical Engineer', 'Mechanical Engineer'), ('Civil Engineer', 'Civil Engineer'), ('Information Technology', 'Information Technology')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='sell_product',
            name='year',
            field=models.CharField(choices=[('3', 'TE'), ('4', 'BE'), ('1', 'FE'), ('2', 'SE')], default='', max_length=50),
        ),
    ]
