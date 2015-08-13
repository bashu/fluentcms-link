# -*- coding: utf-8 -*-

from fluent_contents.extensions import ContentPlugin, plugin_pool

from fluent_pages.models import Page

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
        elif instance.page_link:
            link = instance.page_link.url
        else:
            link = ""

        context = super(LinkPlugin, self).get_context(
            request, instance, **kwargs)

        context.update({
            'link': link, 
        })
        return context    
