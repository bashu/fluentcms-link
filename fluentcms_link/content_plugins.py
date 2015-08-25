# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from fluent_contents.extensions import ContentPlugin, plugin_pool

from .models import LinkItem


@plugin_pool.register
class LinkPlugin(ContentPlugin):
    """
    Plugin for adding a link to an other page or to an external
    website
    """
    model = LinkItem
    render_template = "fluentcms_link/link.html"

    def get_context(self, request, instance, **kwargs):
        if instance.mailto:
            link = u"mailto:%s" % instance.mailto
        elif instance.url:
            link = instance.url
        else:
            link = ""

        context = super(LinkPlugin, self).get_context(
            request, instance, **kwargs)

        context.update({
            'link': link, 
        })
        return context    
