# -*- coding: utf-8 -*-
from plone import api
from Products.Five import BrowserView
from collective.portlet.discussion.utility.interfaces import ICommentsListUtility
from zope.component import getUtility
from zope.interface.interfaces import ComponentLookupError


class View(BrowserView):
    """View for the comments search"""

    def getDiscussionsList(self):
        """return a list of discussions"""
        try:
            utility = getUtility(ICommentsListUtility, name="comments_list_utility")(self.context)
            return utility(self.request.form)
        except ComponentLookupError:
            return []

    @property
    def search_results_description_length(self):
        return api.portal.get_registry_record(
            name="plone.search_results_description_length"
        )

    @property
    def allow_anon_views_about(self):
        return api.portal.get_registry_record(name="plone.allow_anon_views_about")
