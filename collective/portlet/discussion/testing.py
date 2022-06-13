from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneWithPackageLayer

import collective.portlet.discussion


FIXTURE = PloneWithPackageLayer(
    zcml_package=collective.portlet.discussion,
    zcml_filename='configure.zcml',
    gs_profile_id='collective.portlet.discussion:default',
    name="CollectivePortletDiscussionFixture",
)
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="CollectivePortletDiscussion:IntegrationTesting",
)
