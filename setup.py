from setuptools import find_packages, setup

import djangocms_versioning_filer


CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Framework :: Django',
    'Framework :: Django :: 1.11',
    'Framework :: Django :: 2.0',
    'Framework :: Django :: 2.1',
]

INSTALL_REQUIREMENTS = [
    'Django>=1.11,<2.2',
    # 'django-filer',  # new version not released
    # 'djangocms-versioning',  # not released
    # 'django-cms>=4.0',  # not released
]

setup(
    name='djangocms-versioning-filer',
    author='Divio AG',
    author_email='info@divio.ch',
    url='http://github.com/divio/djangocms-versioning-filer',
    license='BSD',
    version=djangocms_versioning_filer.__version__,
    description=djangocms_versioning_filer.__doc__,
    long_description=open('README.rst').read(),
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIREMENTS,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    test_suite='test_settings.run',
)
