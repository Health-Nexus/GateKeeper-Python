

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=200)),
                ('days', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
