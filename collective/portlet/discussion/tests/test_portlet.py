from collective.portlet.discussion import discussionportlet
from collective.portlet.discussion.testing import INTEGRATION_TESTING
from plone import api
from plone.app.discussion.interfaces import IConversation
from plone.app.discussion.interfaces import IDiscussionSettings
from plone.app.portlets.storage import PortletAssignmentMapping
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.portlets.interfaces import IPortletAssignment
from plone.portlets.interfaces import IPortletDataProvider
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import IPortletRenderer
from plone.portlets.interfaces import IPortletType
from unittest import TestCase
from zope.component import createObject
from zope.component import getMultiAdapter
from zope.component import getUtility


def enable_comments():
    api.portal.set_registry_record(
        name="globally_enabled", interface=IDiscussionSettings, value=True
    )


def add_comment(context, text, author_name="Sanderson"):
    conversation = IConversation(context)
    comment = createObject('plone.Comment')
    comment.text = text
    comment.author_name = author_name
    conversation.addComment(comment)


class TestPortlet(TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_portlet_type_registered(self):
        portlet = getUtility(
            IPortletType, name='collective.portlet.discussion.DiscussionPortlet'
        )
        self.assertEquals(
            portlet.addview, 'collective.portlet.discussion.DiscussionPortlet'
        )

    def test_interfaces(self):
        # TODO: Pass any keyword arguments to the Assignment constructor
        portlet = discussionportlet.Assignment()
        self.failUnless(IPortletAssignment.providedBy(portlet))
        self.failUnless(IPortletDataProvider.providedBy(portlet.data))

    def test_invoke_add_view(self):
        portlet = getUtility(
            IPortletType, name='collective.portlet.discussion.DiscussionPortlet'
        )
        mapping = self.portal.restrictedTraverse('++contextportlets++plone.leftcolumn')
        for m in mapping.keys():
            del mapping[m]
        addview = mapping.restrictedTraverse('+/' + portlet.addview)

        # TODO: Pass a dictionary containing dummy form inputs from the add
        # form.
        # Note: if the portlet has a NullAddForm, simply call
        # addview() instead of the next line.
        addview.createAndAdd(data={})

        self.assertEquals(len(mapping), 1)
        self.failUnless(
            isinstance(list(mapping.values())[0], discussionportlet.Assignment)
        )

    def test_invoke_edit_view(self):
        # NOTE: This test can be removed if the portlet has no edit form
        mapping = PortletAssignmentMapping()
        request = self.layer['request']

        mapping['foo'] = discussionportlet.Assignment()
        editview = getMultiAdapter((mapping['foo'], request), name='edit')
        self.failUnless(isinstance(editview, discussionportlet.EditForm))

    def test_obtain_renderer(self):
        folder = api.content.create(
            container=self.portal, type='Folder', title='Folder'
        )
        request = folder.REQUEST
        view = folder.restrictedTraverse('@@plone')
        manager = getUtility(
            IPortletManager, name='plone.rightcolumn', context=self.portal
        )

        # TODO: Pass any keyword arguments to the Assignment constructor
        assignment = discussionportlet.Assignment()

        renderer = getMultiAdapter(
            (folder, request, view, manager, assignment), IPortletRenderer
        )
        self.failUnless(isinstance(renderer, discussionportlet.Renderer))

    def test_renderer_multiple_comment(self):
        enable_comments()
        folder = api.content.create(
            container=self.portal,
            type='Folder',
            title='Did you write any books?',
        )
        add_comment(folder, "Yes, I have written a few fantasy books.")
        view = folder.restrictedTraverse('@@discussion_list_search')
        output = view()
        self.assertIn("Comment search", output)
        self.assertIn("Sanderson on Did you write any books?", output)
        self.assertIn("Yes, I have written a few fantasy books.", output)


class TestRenderer(TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.folder = api.content.create(
            container=self.portal,
            type='Folder',
            title='Folder',
        )

    def renderer(
        self, context=None, request=None, view=None, manager=None, assignment=None
    ):
        context = context or self.folder
        request = request or self.folder.REQUEST
        view = view or self.folder.restrictedTraverse('@@plone')
        manager = manager or getUtility(
            IPortletManager, name='plone.rightcolumn', context=self.portal
        )

        # TODO: Pass any default keyword arguments to the Assignment
        # constructor.
        assignment = assignment or discussionportlet.Assignment()
        return getMultiAdapter(
            (context, request, view, manager, assignment), IPortletRenderer
        )

    def test_renderer_no_comments(self):
        renderer = self.renderer()
        output = renderer.render()
        # Note: I could imagine we make the output empty if comments are disabled.
        # But then why install this package?
        self.assertIn("discussionPortlet", output)
        self.assertIn("portletHeader", output)
        self.assertIn("Discussions", output)

    def test_renderer_one_comment(self):
        enable_comments()
        add_comment(self.folder, "First post!")
        renderer = self.renderer()
        output = renderer.render()
        self.assertIn("discussionPortlet", output)
        self.assertIn("portletHeader", output)
        self.assertIn("Discussions", output)
        # The author name and title of the context appear:
        self.assertIn("Sanderson on Folder", output)
        # There is no link to the full list:
        self.assertNotIn("discussion_list_search", output)

    def test_renderer_multiple_comment(self):
        enable_comments()
        for num in range(6):
            add_comment(self.folder, "Comment {}".format(num))
        renderer = self.renderer()
        output = renderer.render()
        self.assertIn("Discussions", output)
        # The author name and title of the context appear:
        self.assertIn("Sanderson on Folder", output)
        # There is a link to the full list:
        self.assertIn("discussion_list_search", output)
