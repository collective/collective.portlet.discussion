from Acquisition import aq_get
from collective.portlet.discussion import DiscussionPortletMessageFactory as _
from zope.i18n import translate
from zope.interface import implementer
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary


@implementer(IVocabularyFactory)
class DiscussionStatesVocabulary(object):
    """
    A simple vocab to translate the discussion states
    """

    def __call__(self, context):
        context = getattr(context, 'context', context)
        request = aq_get(context, 'REQUEST', None)

        return SimpleVocabulary.fromItems(((translate(_('Pending'), context=request), 'pending'),
                                           (translate(_('Published'), context=request), 'published')))

DiscussionStatesVocabularyFactory = DiscussionStatesVocabulary()
