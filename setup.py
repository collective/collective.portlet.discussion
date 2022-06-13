from setuptools import find_packages
from setuptools import setup


with open("README.rst") as myfile:
    long_description = myfile.read()
with open("CHANGES.rst") as myfile:
    long_description += "\n" + myfile.read()

version = "2.0.0a1"

setup(
    name="collective.portlet.discussion",
    version=version,
    description="A simple Plone portlet to show a list of comments",
    long_description=long_description,
    # Get more strings from https://pypi.org/classifiers/
    classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="discussion portlet comments",
    author="RedTurtle Technology",
    author_email="sviluppoplone@redturtle.it",
    maintainer="Maurits van Rees",
    maintainer_email="m.van.rees@zestsoftware.nl",
    url="https://github.com/collective/collective.portlet.discussion",
    license="GPL",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["collective", "collective.portlet"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "plone.api",
        "plone.app.discussion",
        "six",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
        ]
    },
    entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
)
