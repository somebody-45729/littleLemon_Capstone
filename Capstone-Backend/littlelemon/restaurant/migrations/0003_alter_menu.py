from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_bookings.py'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'verbose_name': 'Menu', 'verbose_name_plural': 'Menu Items'},
        ),
    ]