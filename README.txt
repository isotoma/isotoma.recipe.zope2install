isotoma.recipe.zope2install
===========================

THIS IS A FORK OF ``plone.recipe.zope2install`` TO MAKE IT USE THE BUILDOUT
DOWNLOAD API.


Options
-------

To specify which Zope 2 to use, use one of the following options:

`url`
    The URL to a tarball to use for the Zope 2 installation.

`svn`
    The URL for an subversion checkout to use for the Zope 2 installation.

`location`
    The path to a local, existing Zope 2 installation. Note: For this to work
    Zope must have been built with the same Python used to run buildout.

`fake-zope-eggs`
    If set to true, add fake egg links to Zope 3 libraries, so that setuptools
    can see and use them for dependencies lookup. Enabled by default since
    version 3.0 of this recipe.

`additional-fake-eggs`
    Specify an optional list of additional fake eggs. Only include packages
    which are available on the Python path.

    You can also specify an explicit version to fake for an egg. For example::

        additional-fake-eggs =
            ZODB3 = 3.7.1
            zope.annotation = 3.3.2

    Otherwise the faked eggs will always have version 0.0.
    
    The default value includes Acquisition, ClientForm, DateTime, docutils,
    ExtensionClass, mechanize, Persistence, pytz, RestrictedPython,
    tempstorage, ZConfig, zLOG, zodbcode, ZODB3, zdaemon and Zope2.

`skip-fake-eggs`
    Specify an optional list of packages, for whom no fake egg is created.
    This allows to pull in new versions of some of the Zope packages via
    normal version requirements.

`smart-recompile`
    Will not recompile Zope if it finds .so or .pyd files. This means
    you can move your buildout around and speed up builds.

`python`
    Specify a section that configures another executable than the one used by 
    ``bin/buildout``.  For example::

        [zope2]
        recipe = isotoma.recipe.zope2install
        ...
        python = python2.4
        
        [python2.4]
        executable = ${buildout:directory}/parts/python/bin/python

If you use many buildouts with the same Zope 2 version, then you can add
"zope-directory" in the "buildout" section in your ~/.buildout/default.cfg
file like this::

    [buildout]
    zope-directory = /home/me/buildout/zope

For installations from a tarball that directory will be used instead of the
parts directory in your buildout. Each version of Zope will get it's own
directory but if it's already installed the existing one will be reused.

Exported variables
------------------

The following variables are set by this recipe and can be used in other parts.

`location`
    The path to the Zope installation root.

Reporting bugs or asking questions
----------------------------------

Please report bugs on GitHub.

