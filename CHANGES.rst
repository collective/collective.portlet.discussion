Changelog
=========

2.0.0a2 (2023-08-31)
--------------------

- Fix CI, test on all supported combinations:
  Plone 5.2 on Python 2.7 and 3.8.
  Plone 6.0 on Python 3.8-3.11.
  [maurits]

- Explicitly load CMFCore permissions early.
  This avoids a startup error, depending on the order the packages are loaded.
  [maurits]


2.0.0a1 (2022-06-13)
--------------------

- Removed workflows: the default Plone 5.2+ ones are the same or better.
  Fixes `issue 3 <https://github.com/collective/collective.portlet.discussion/issues/3>`_.
  [maurits]

- Moved to the `Plone collective <https://github.com/collective/collective.portlet.discussion>`_.
  See `small discussion <https://github.com/RedTurtle/collective.portlet.discussion/pull/5>`_.
  [maurits]

- Add 5.2 and 6.0 compatibility, on Python 2 and 3.  [maurits]

- Drop Plone 3 and 4 compatibility.  [maurits]


1.2.6 (2019-05-13)
------------------

- Support Dexterity in the folder widget to show comments only for a specific subtree in the site. [fredvd]


1.2.5 (2017-04-28)
------------------

- Fix translations for discussion_list_search. [fredvd]


1.2.4 (2017-01-25)
------------------

- Add Dutch translations
  [fredvd]


1.2.3 (2016-04-04)
------------------

- Fixed tests [cekk]
- Bugfix, isAnon missing [tobiasherp]
- pep8ification, formatting [tobiasherp]


1.2.2 (2013-11-07)
------------------

- Fixed imports in template [andrea]


1.2.1 (2013-07-26)
------------------

- Added class tile to portlet header [andrea]


1.2.0 (2013-06-26)
------------------

- Added support for Site Administrator role [keul]

1.1.0 (2012-11-23)
------------------

* Added new workflows for Discussion Items [micecchi]
* Plone 4 compatibility [micecchi]

1.0.1 (2011-07-10)
------------------

* Fixed filtered results [micecchi]

1.0.0 (2011-01-20)
------------------

* Initial release [micecchi]
