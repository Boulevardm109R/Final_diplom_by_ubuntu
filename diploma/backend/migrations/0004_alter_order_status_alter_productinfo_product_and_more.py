
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_alter_shop_filename_alter_shop_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('confirmed', 'подтвержден'), ('canceled', 'отменен'), ('in_process', 'в процессе выбора клиентом'), ('paid', 'оплачен'), ('assembly', 'в процессе сборки'), ('in delivery', 'передан в службу доставки'), ('in client', 'доставлен')], default='in_process', max_length=35, verbose_name='Статус заказа'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_infos', to='backend.product', verbose_name='Продукт'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_infos', to='backend.shop', verbose_name='Магазин'),
        ),
    ]