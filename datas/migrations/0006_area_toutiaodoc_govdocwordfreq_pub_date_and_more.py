# Generated by Django 4.2 on 2023-04-23 13:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("datas", "0005_datatype"),
    ]

    operations = [
        migrations.CreateModel(
            name="Area",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="ToutiaoDoc",
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
                ("area", models.CharField(blank=True, max_length=50)),
                ("search_keyword", models.CharField(blank=True, max_length=50)),
                ("link", models.TextField(blank=True)),
                ("title", models.CharField(blank=True, max_length=500)),
                ("pub_date", models.DateTimeField(blank=True, null=True)),
                ("source", models.CharField(blank=True, max_length=50)),
                ("context", models.TextField(blank=True)),
                ("comment", models.TextField(blank=True)),
                ("is_split", models.BooleanField(blank=True, default=False)),
            ],
            options={
                "unique_together": {("area", "title", "pub_date")},
            },
        ),
        migrations.AddField(
            model_name="govdocwordfreq",
            name="pub_date",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="ToutiaoDocWordFreqAggr",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("word", models.CharField(max_length=500)),
                ("freq", models.IntegerField(default=0)),
                ("area", models.CharField(default="TOTAL", max_length=50)),
            ],
            options={
                "unique_together": {("word", "area")},
            },
        ),
        migrations.CreateModel(
            name="ToutiaoDocWordFreq",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                ("word", models.CharField(max_length=500)),
                ("freq", models.IntegerField(default=0)),
                ("pub_date", models.DateTimeField(blank=True, null=True)),
                (
                    "record",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="datas.toutiaodoc",
                    ),
                ),
            ],
            options={
                "unique_together": {("word", "record_id")},
            },
        ),
    ]
