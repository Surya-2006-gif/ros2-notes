from setuptools import find_packages, setup
from glob import glob
import os

package_name = 'week1'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),  # Make sure this file exists
        ('share/' + package_name, ['package.xml']),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='surya',
    maintainer_email='surya@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = week1.publisher:main',
            'listener = week1.subscriber:main',
            'launch_ = week1.game_publisher:main',
        ],
    },
)
