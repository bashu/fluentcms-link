fluentcms-link
==============

.. image:: https://img.shields.io/pypi/v/fluentcms-link.svg
    :target: https://pypi.python.org/pypi/fluentcms-link/

.. image:: https://img.shields.io/pypi/dm/fluentcms-link.svg
    :target: https://pypi.python.org/pypi/fluentcms-link/

.. image:: https://img.shields.io/github/license/bashu/fluentcms-link.svg
    :target: https://pypi.python.org/pypi/fluentcms-link/

.. image:: https://img.shields.io/travis/bashu/fluentcms-link.svg
    :target: https://travis-ci.com/github/bashu/fluentcms-link/

A plugin for django-fluent-contents_ to add a link to an other page or
to an external website.

Installation
------------

First install the module, preferably in a virtual environment. It can be installed from PyPI:

.. code-block:: shell

    pip install fluentcms-link


Backend Configuration
~~~~~~~~~~~~~~~~~~~~~

First make sure the project is configured for django-fluent-contents_.

Then add the following settings:

.. code-block:: python

    INSTALLED_APPS += (
        'fluentcms_link',
    )

The database tables can be created afterwards:

.. code-block:: shell

    python ./manage.py migrate

Now, the ``LinkPlugin`` can be added to your ``PlaceholderField`` and
``PlaceholderEditorAdmin`` admin screens.

Frontend Configuration
~~~~~~~~~~~~~~~~~~~~~~

If needed, the HTML code can be overwritten by redefining ``fluentcms_link/link.html``.

Contributing
------------

If you like this module, forked it, or would like to improve it, please let us know!
Pull requests are welcome too. :-)

.. _django-fluent-contents: https://github.com/edoburu/django-fluent-contents
