# Generated by Django 4.1.7 on 2023-02-24 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_options_alter_tag_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Тэг'),
        ),
    ]
