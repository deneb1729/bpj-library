# Generated by Django 3.1.7 on 2021-03-05 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
        ("catalog", "0004_auto_20210223_1757"),
    ]

    operations = [
        migrations.RenameField(
            model_name="bookinstance",
            old_name="imprint",
            new_name="editorial",
        ),
        migrations.RemoveField(
            model_name="book",
            name="author",
        ),
        migrations.AddField(
            model_name="book",
            name="author",
            field=models.ManyToManyField(related_name="books", to="catalog.Author"),
        ),
        migrations.AlterField(
            model_name="bookinstance",
            name="borrower",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.partner",
            ),
        ),
        migrations.AlterField(
            model_name="bookinstance",
            name="status",
            field=models.CharField(
                blank=True,
                choices=[("a", "Available"), ("b", "Borrowed"), ("m", "Maintenance")],
                default="a",
                help_text="Disponibilidad del libro",
                max_length=1,
            ),
        ),
    ]