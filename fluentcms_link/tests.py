from django.test import TestCase
from fluent_contents.tests.factories import create_content_item
from fluent_contents.tests.utils import render_content_items

from fluentcms_link.models import LinkItem


class LinkTests(TestCase):
    """
    Testing link plugin
    """

    def test_output(self):
        """
        Test the standard link
        """
        item = create_content_item(LinkItem, url="http://example.com", name="TEST")
        self.assertHTMLEqual(
            render_content_items([item]).html,
            '<span class="link">'
            '<a href="http://example.com">'
            'TEST'
            '</a>'
            "</span>",
        )
