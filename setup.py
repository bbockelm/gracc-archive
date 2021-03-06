from setuptools import setup, find_packages
import os


setup(name='graccarchive',
      version='1.4.0',
      description='GRACC Archive Agent',
      author_email='dweitzel@cse.unl.edu',
      author='Derek Weitzel',
      url='https://opensciencegrid.github.io/gracc',
      package_dir={'': 'src'},
      packages=['graccarchive'],
      install_requires=['pika',
      'six',
      'toml',
      'urllib3',
      'wsgiref'
      ],
      entry_points= {
            'console_scripts': [
                  'graccarchiver = graccarchive.graccarchive:main',
                  'graccunarchiver = graccarchive.unarchive:main'
            ]
      }
)
