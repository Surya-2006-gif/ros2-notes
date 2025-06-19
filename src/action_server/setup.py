from setuptools import find_packages, setup
import os
import glob
package_name = 'action_server'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name,'launch'),glob.glob('launch/*'))
    ],
    install_requires=['setuptools','action_interface'],
    zip_safe=True,
    maintainer='surya',
    maintainer_email='suryaatphase2@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rotation_client=action_server.rotation_client:main',
            'rotation_server=action_server.rotation_server:main',
            'publisher=action_server.simple_publisher:main',
            'subscriber=action_server.simple_subscriber:main',
        ],
    },
)
