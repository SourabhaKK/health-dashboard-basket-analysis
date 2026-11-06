"""
Setup script for the health dashboard and basket analysis project
"""

from setuptools import setup, find_packages

setup(
    name="health-dashboard-basket-analysis",
    version="1.0.0",
    author="Sourabha K Kallapur",
    description="Health data dashboard and supermarket basket analysis",
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'pandas>=2.0.3',
        'numpy>=1.24.3',
        'matplotlib>=3.7.2',
        'requests>=2.31.0',
        'pytest>=7.4.0',
        'pytest-cov>=4.1.0',
        'colorama>=0.4.6',
        'pypdf>=6.4.1'
    ],
)
