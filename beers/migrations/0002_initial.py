# Generated by Django 4.1.1 on 2022-10-02 22:31
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ("beers", "0001_initial"),
    ]
    operations = [
        migrations.CreateModel(
            name="Bar",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("order_date", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Reference",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("ref", models.CharField(blank=True, max_length=255, null=True)),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                (
                    "bar",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="beers.bar",
                    ),
                ),
                (
                    "order",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="beers.order",
                    ),
                ),
                (
                    "reference",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="beers.reference",
                    ),
                ),
                ("count", models.BigIntegerField(default=1)),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.CreateModel(
            name="Stock",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("stock", models.BigIntegerField(blank=True, null=True)),
                (
                    "bar",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="beers.bar",
                    ),
                ),
                (
                    "reference",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="beers.reference",
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
            },
        ),
        migrations.AlterField(
            model_name="OrderItem",
            name="order",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="beers.order",
            ),
        ),
    ]
