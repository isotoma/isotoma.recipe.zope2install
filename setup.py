import os
from setuptools import setup, find_packages

name = "isotoma.recipe.zope2install"
version = '0.0'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
        read('README.txt')
        + '\n' +
        read('CHANGES.txt'))

setup(
    name=name,
    version=version,
    maintainer = "John Carr",
    maintainer_email = "john.carr@isotoma.com",
    description="ZC Buildout recipe for installing Zope 2.",
    long_description=long_description,
    license="ZPL 2.1",
    keywords="zope2 buildout",
    url = 'http://github.com/isotoma/isotoma.recipe.zope2install',
    classifiers = [
      "License :: OSI Approved :: Zope Public License",
      "Framework :: Buildout",
      "Framework :: Buildout :: Recipe",
      "Framework :: Plone",
      "Framework :: Zope2",
      "Programming Language :: Python",
      ],
    packages=find_packages(),
    include_package_data=True,
    namespace_packages=['isotoma', 'isotoma.recipe'],
    install_requires=['zc.buildout', 'setuptools'],
      extras_require=dict(
            test=[
                  'zope.testing',
                 ]),
    zip_safe=False,
    entry_points={'zc.buildout': ['default = isotoma.recipe.zope2install:Recipe']},
    )
