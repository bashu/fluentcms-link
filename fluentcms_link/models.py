# -*- coding: utf-8 -*-

from future.utils import python_2_unicode_compatible

from django.db import models
from django.utils.translation import ugettext_lazy as _

from fluent_contents.extensions import PluginUrlField
from fluent_contents.models.db import ContentItem


@python_2_unicode_compatible
class LinkItem(ContentItem):

    name = models.CharField(_("name"), max_length=256)
    url = PluginUrlField(_("URL"), null=True, blank=True)
    mailto = models.EmailField(_("mailto"), blank=True, null=True,
        help_text=_("An email adress has priority over a text or page link."))

    target = models.CharField(_("target"), blank=True, max_length=100, choices=((
        ("", _("same window")),
        ("_blank", _("new window")),
        ("_parent", _("parent window")),
        ("_top", _("topmost frame")),
    )))
    
    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Links")

    def __str__(self):
        return self.name
