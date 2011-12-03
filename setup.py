import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = ['pyramid', 'pyramid_debugtoolbar', 'pyramid_jinja2']

setup(name='vprohoda.com',
      version='0.1',
      description='vprohoda.com',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Vladimir Prohoda',
      author_email='i@vprohoda.com',
      url='http://vprohoda.com',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="vprohodacom",
      entry_points = """\
      [paste.app_factory]
      main = vprohodacom:main
      """,
      paster_plugins=['pyramid'],
      )

