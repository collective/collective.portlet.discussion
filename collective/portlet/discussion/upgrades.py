from Products.CMFCore.utils import getToolByName
from collective.portlet.discussion import logger
from zope.component import getMultiAdapter

default_profile = 'profile-collective.portlet.discussion:default'


def upgrade(upgrade_product, version):
    """ Decorator for updating the QuickInstaller of a upgrade """

    def wrap_func(fn):
        def wrap_func_args(context, *args):
            p = getToolByName(context, 'portal_quickinstaller').get(upgrade_product)
            setattr(p, 'installedversion', version)
            return fn(context, *args)
        return wrap_func_args
    return wrap_func


@upgrade('collective.portlet.discussion', '1.1.0')
def to_1_1_0(context):
    """
    Create new workflows for comments, and update existing comments
    """
    logger.info('Upgrading collective.portlet.discussion to version 1.1.0')
    context.runImportStepFromProfile(default_profile, 'workflow')
    logger.info('Reinstalled workflow.xml')
    wftool = getMultiAdapter((context, context.REQUEST), name=u"plone_tools").workflow()
    brains = context.portal_catalog(portal_type="Discussion Item")
    for brain in brains:
        obj = brain.getObject()
        chain = wftool.getChainFor(obj)
        if chain:
            wf_id = chain[0]
            wf = wftool.getWorkflowById(wf_id)
            wf.updateRoleMappingsFor(obj)
            obj.reindexObjectSecurity()
    logger.info("updated %d Discussion Items" % len(brains))
