# Generated by Django 4.2 on 2023-04-24 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datas", "0007_area_level"),
    ]

    operations = [
        migrations.CreateModel(
            name="WeiboDoc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("city", models.CharField(max_length=200)),
                ("time", models.CharField(blank=True, max_length=100, null=True)),
                ("month", models.CharField(blank=True, max_length=100, null=True)),
                ("mblogurl", models.CharField(max_length=2000)),
                ("mid", models.IntegerField()),
                ("user_id", models.CharField(max_length=100)),
                ("user_name", models.CharField(max_length=100)),
                ("source", models.CharField(max_length=100)),
                ("user_gender", models.CharField(max_length=10)),
                ("user_statuses_count", models.IntegerField()),
                ("user_followers_count", models.CharField(max_length=100)),
                ("user_follow_count", models.CharField(max_length=100)),
                ("user_verified", models.BooleanField()),
                ("user_verified_type", models.IntegerField()),
                ("user_verified_reason", models.CharField(max_length=1000)),
                ("user_urank", models.IntegerField()),
                ("location", models.CharField(max_length=1000)),
                ("content", models.TextField(blank=True)),
                ("length", models.IntegerField()),
                ("is_splmt", models.IntegerField()),
                ("splmt_type", models.CharField(max_length=100)),
                ("splmt_title", models.CharField(max_length=500)),
                ("splmt_url", models.CharField(max_length=1000)),
                ("urls_num", models.IntegerField()),
                ("reposts_count", models.IntegerField()),
                ("comments_count", models.IntegerField()),
                ("attitudes_count", models.IntegerField()),
                ("pic_num", models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name="area",
            name="name",
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
