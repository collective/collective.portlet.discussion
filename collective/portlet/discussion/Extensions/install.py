# -*- coding: utf-8 -*-

from collective.portlet.discussion import logger
from zope.component import getMultiAdapter


def install(portal, reinstall=False):
    setup_tool = portal.portal_setup
    setup_tool.runAllImportStepsFromProfile('profile-collective.portlet.discussion:default')
    if not reinstall:
        updateDiscussionStates(portal)


def uninstall(portal, reinstall=False):
    setup_tool = portal.portal_setup
    if not reinstall:
        setup_tool.runAllImportStepsFromProfile('profile-collective.portlet.discussion:uninstall')
        setup_tool.runAllImportStepsFromProfile('profile-plone.app.discussion:default')
        updateDiscussionStates(portal)


def updateDiscussionStates(portal):
    """
    search all discussions in the portal and update security info.
    """
    catalog = portal.portal_catalog
    brains = catalog(portal_type="Discussion Item")
    wftool = getMultiAdapter((portal, portal.REQUEST), name=u"plone_tools").workflow()
    for brain in brains:
        obj = brain.getObject()
        chain = wftool.getChainFor(obj)
        if chain:
            wf_id = chain[0]
            wf = wftool.getWorkflowById(wf_id)
            wf.updateRoleMappingsFor(obj)
            obj.reindexObjectSecurity()
    logger.info("updated workflow for %d Discussion Items" % len(brains))
