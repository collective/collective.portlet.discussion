Introduction
============

This is a portlet is a plugin for `plone.app.discussion <http://pypi.python.org/pypi/plone.app.discussion>`_
that show last comments in the portal.

You can select to filter comments by state (if comments are moderated)

Workflow
========
This product creates two new workflows for comments: **comment_one_state_workflow** and **comment_review_workflow**.

With these workflows, comments inherits security settings from parents. In this way users that can't access to certain contents doesn't see them comments in the portlet.

Installing this product, security settings for old discussions will be updated. Same thing on uninstall step.

Dependencies
============

This product has been tested on Plone 3.3.5 and Plone 4.2

Credits
=======

Developed with the support of `Regione Emilia Romagna`__; Regione Emilia Romagna supports the `PloneGov initiative`__.

__ http://www.regione.emilia-romagna.it/
__ http://www.plonegov.it/

Authors
=======

This product was developed by RedTurtle Technology team.

.. image:: http://www.redturtle.net/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.net/


