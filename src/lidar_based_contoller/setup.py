from setuptools import find_packages, setup

package_name = 'lidar_based_contoller'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='surya',
    maintainer_email='suryaatphase2@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lidar_stopper = lidar_based_contoller.distance_measurer:main',
            'maze_solver = lidar_based_contoller.maze_solver:main'
        ],
    },
)
