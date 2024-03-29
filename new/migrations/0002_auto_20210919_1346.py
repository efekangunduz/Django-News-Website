# Generated by Django 3.2.7 on 2021-09-19 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('new', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new.new')),
            ],
        ),
    ]
