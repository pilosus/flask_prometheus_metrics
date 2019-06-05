from setuptools import setup, find_packages
from version import get_version
from pathlib import Path

current_dir = Path(__file__).resolve().parent
description = 'Prometheus Metrics for Flask Web App'

try:
    history = current_dir.joinpath('CHANGELOG.md').read_text()
    long_description = '\n\n'.join([current_dir.joinpath('README.md').read_text(), history])
except FileNotFoundError:
    long_description = 'Prometheus Metrics for Flask Web Application using official Prometheus Python client'

setup(
    name='flask_prometheus_metrics',
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Flask',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
    ],
    author='Vitaly R. Samigullin',
    author_email='vrs@pilosus.org',
    url='https://github.com/pilosus/flask_prometheus_metrics/',
    version=get_version(),
    license='MIT',
    python_requires='>=3.6',
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'prometheus-client>=0.6.0',
    ],
    extras_require={
        'flask': ['Flask>=1.0.0'],
    }
)
