from zope.i18nmessageid import MessageFactory
CommentPortletMessageFactory = MessageFactory('collective.portlet.discussion')

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
