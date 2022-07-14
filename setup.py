from setuptools import setup, find_packages
import os

version = '2.0.0'

setup(name='collective.portlet.discussion',
      version=version,
      description="A simple Plone portlet to show a list of comments",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Development Status :: 5 - Beta",
        "Programming Language :: Python",
        "Programming Language :: Python 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='discussion portlet comments',
      author='RedTurtle Technology',
      author_email='sviluppoplone@redturtle.it',
      url='https://github.com/RedTurtle/collective.portlet.discussion',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.portlet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.discussion',
      ],
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
