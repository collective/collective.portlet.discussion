# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName


class CommentsListUtility(object):
    """
    A simple vocab to translate the discussion states
    """

    def __init__(self, context):
        self.context = context

    def __call__(self, query):
        pc = getToolByName(self.context, 'portal_catalog')
        if not pc:
            return []
        return pc(**query)
