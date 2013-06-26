Introduction
============

This is a portlet is a plugin for `plone.app.discussion <http://pypi.python.org/pypi/plone.app.discussion>`_
that show last comments in the portal.

You can select to filter comments by state (if comments are moderated) and also a starting path for searches.

Workflow
========

This product creates two new workflows for comments: **comment_one_state_workflow** and **comment_review_workflow**.

With these workflows, comments inherits security settings from parents, fixing a Plone issue.
In this way an user that can't see a content doesn't have catalog access to related comments, so comments are not visibile
in the portlet.

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

.. image:: http://www.redturtle.it/redturtle_banner.png
   :alt: RedTurtle Technology Site
   :target: http://www.redturtle.it/


