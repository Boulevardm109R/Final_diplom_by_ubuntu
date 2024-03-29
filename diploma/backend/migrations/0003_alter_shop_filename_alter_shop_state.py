from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_shop_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='filename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Магазин принимает заказы'),
        ),
    ]