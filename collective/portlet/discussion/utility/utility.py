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
        #filter comments to show only comments of objects that the user can view
        # uids=[x.UID for x in all_comments]
        # portal_types = getToolByName(self.context, 'portal_types')
        # portal_properties = getToolByName(self.context, 'portal_properties')
        # site_properties = getattr(portal_properties, 'site_properties')
        # if site_properties.hasProperty('types_not_searched'):
        #     search_types=[x for x
        #                   in portal_types.keys()

        #                   if x not in site_properties.getProperty('types_not_searched')]
        # objects_commented = pc(UID=uids,portal_type=search_types)
        # available_uids=[x.UID for x in objects_commented]
        # filtered_comments=[x for x in all_comments if x.UID in available_uids]
        # return filtered_comments
