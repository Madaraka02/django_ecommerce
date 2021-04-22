# Generated by Django 3.2 on 2021-04-19 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shucks', '0003_advert'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shucks.color')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shucks.product')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shucks.size')),
            ],
        ),
    ]