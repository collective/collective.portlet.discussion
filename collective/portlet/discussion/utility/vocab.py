try:
    from zope.app.schema.vocabulary import IVocabularyFactory
except ImportError:
    from zope.schema.interfaces import IVocabularyFactory
from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.i18n import translate
from Acquisition import aq_get
from collective.portlet.discussion import DiscussionPortletMessageFactory as _


class DiscussionStatesVocabulary(object):
    """
    A simple vocab to translate the discussion states
    """
    implements(IVocabularyFactory)

    def __call__(self, context):
        context = getattr(context, 'context', context)
        request = aq_get(context, 'REQUEST', None)

        return SimpleVocabulary.fromItems(((translate(_('Pending'), context=request), 'pending'),
                                           (translate(_('Published'), context=request), 'published')))

DiscussionStatesVocabularyFactory = DiscussionStatesVocabulary()
