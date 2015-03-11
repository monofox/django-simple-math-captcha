from setuptools import setup, find_packages
import os, glob

try:
    README = open('README.rst').read()
except:
    README = None

translationFiles = []
for module in find_packages():
    if os.path.exists(os.path.join(module, 'locale')):
        translationFiles += [os.path.join(module, 'locale', lang) for lang in os.listdir(os.path.join(module, 'locale'))]
data_files = [(os.path.join(path, 'LC_MESSAGES'),
    glob.glob(os.path.join(path, 'LC_MESSAGES', 'django*'))) for path in translationFiles]

setup(
    name='django-simple-math-captcha',
    version=__import__('simplemathcaptcha').__version__,
    description='An easy-to-use math field/widget captcha for Django forms.',
    long_description=README,
    author='Brandon Taylor',
    author_email='alsoicode@gmail.com',
    url='https://brandonftaylor.com/',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    data_files=data_files,
    classifiers=['Development Status :: 5 - Production/Stable',
               'Environment :: Web Environment',
               'Framework :: Django',
               'Intended Audience :: Developers',
               'License :: OSI Approved :: Apache Software License',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: Implementation :: CPython',
               'Topic :: Utilities'],
    install_requires=["Django >= 1.4"],
)
