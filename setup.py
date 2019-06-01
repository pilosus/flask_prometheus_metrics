from setuptools import setup, find_packages

VERSION = "0.1.0"

setup(
    name='flask_prometheus_metrics',
    description='Prometheus Metrics for Flask Web App',
    long_description='Prometheus Metrics for Flask Web Application using official Prometheus Python client',
    author='Vitaly R. Samigullin',
    author_email='vrs@pilosus.org',
    url='https://github.com/pilosus/flask_prometheus_metrics/',
    version=VERSION,
    python_requires='>=3.6',
    zip_safe=True,
    include_package_data=True,
    packages=find_packages(exclude=['tests']),
    namespace_packages=['flask_prometheus_metrics'],
)
