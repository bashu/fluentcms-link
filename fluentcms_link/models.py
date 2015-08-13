# -*- coding: utf-8 -*-

from future.utils import python_2_unicode_compatible

from django.db import models
from django.utils.translation import ugettext_lazy as _

from fluent_contents.models.db import ContentItem

from fluent_pages.models import Page


@python_2_unicode_compatible
class LinkItem(ContentItem):
    """
    A link to an other page or to an external website
    """
    
    name = models.CharField(_("name"), max_length=256)
    url = models.URLField(_("link"), blank=True, null=True)
    page_link = models.ForeignKey(Page, verbose_name=_("page"), blank=True, null=True,
        help_text=_("A link to a page has priority over a text link."),
        limit_choices_to={'status': status=Page.DRAFT},
    mailto = models.EmailField(_("mailto"), blank=True, null=True,
        help_text=_("An email adress has priority over a text link."))

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
