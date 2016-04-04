# -*- coding: utf-8 -*-
from Products.Five import BrowserView
from collective.portlet.discussion.utility.interfaces import ICommentsListUtility
from zope.component import getUtility
from zope.component.interfaces import ComponentLookupError


class View(BrowserView):
    """View for the comments search"""

    def getDiscussionsList(self):
        """return a list of discussions"""
        try:
            utility = getUtility(ICommentsListUtility, name="comments_list_utility")(self.context)
            return utility(self.request.form)
        except ComponentLookupError:
            return []
