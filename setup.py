from setuptools import setup

desc = 'aojtools is a toolset for aoj, aizu online judge system(http://rose.u-aizu.ac.jp/onlinejudge/) written in Python, including transparently API acccess, problem submit tool and CLI script.'
ldesc = desc

setup(
    name='aojtools'
    , version='0.1.0'
    , description=desc
    , long_description=ldesc
    , classifiers = [
        'Programming Language :: Python'
        , 'Topic :: Internet :: WWW/HTTP'
        , 'Topic :: Software Development :: Libraries :: Python Modules'
    ]
    , author='yatt'
    , author_email='darknesssharp@gmail.com'
    , namespace_packages=['api', 'submit']
    , license='MIT'
)

