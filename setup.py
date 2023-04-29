import setuptools
import gqylpy_command as g

with open(g.__file__, encoding='utf8') as f:
    for line in f:
        if line.startswith('@version: ', 4):
            version = line.split()[-1]
            break
    author, email = f.readline().split(maxsplit=1)[-1].rstrip().split()
    source = f.readline().split()[-1]

setuptools.setup(
    name=g.__name__,
    version=version,
    author=author,
    author_email=email,
    license='Apache 2.0',
    url='http://gqylpy.com',
    project_urls={'Source': source},
    description='调用系统命令，基于内置库 subprocess。并提供了多种用于判断命令调用结果'
                '是否如期的方法。',
    long_description=open('README.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    packages=[g.__name__],
    python_requires='>=3.6, <4',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Utilities',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ]
)
