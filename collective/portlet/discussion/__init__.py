from zope.i18nmessageid import MessageFactory

import logging


logger = logging.getLogger("collective.portlet.discussion")
DiscussionPortletMessageFactory = MessageFactory("collective.portlet.discussion")


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
