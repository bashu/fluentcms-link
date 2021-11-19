import fluent_contents.extensions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fluent_contents", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="LinkItem",
            fields=[
                (
                    "contentitem_ptr",
                    models.OneToOneField(
                        parent_link=True,
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        to="fluent_contents.ContentItem",
                        on_delete=models.CASCADE,
                    ),
                ),
                ("name", models.CharField(max_length=256, verbose_name="name")),
                (
                    "url",
                    fluent_contents.extensions.PluginUrlField(
                        max_length=300, null=True, verbose_name="URL", blank=True
                    ),
                ),
                (
                    "mailto",
                    models.EmailField(
                        help_text="An email adress has priority over a text or page link.",
                        max_length=75,
                        null=True,
                        verbose_name="mailto",
                        blank=True,
                    ),
                ),
                (
                    "target",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        verbose_name="target",
                        choices=[
                            (b"", "same window"),
                            (b"_blank", "new window"),
                            (b"_parent", "parent window"),
                            (b"_top", "topmost frame"),
                        ],
                    ),
                ),
            ],
            options={
                "db_table": "contentitem_fluentcms_link_linkitem",
                "verbose_name": "Link",
                "verbose_name_plural": "Links",
            },
            bases=("fluent_contents.contentitem",),
        ),
    ]
