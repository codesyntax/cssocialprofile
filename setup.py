from setuptools import setup, find_packages
import sys, os

version = '0.7'

setup(name='cssocialprofile',
      version=version,
      description="",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Josu Azpillaga',
      author_email='jazpillaga@codesyntax.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'django-social-auth',
          'django-registration',
          'tweepy',
          'pyfacebook'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
