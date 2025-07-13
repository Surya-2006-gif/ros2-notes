from setuptools import find_packages, setup

package_name = 'opencv_ros'

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
            'polygon_approx = opencv_ros.polygon_approx:main',
            'corner_detection = opencv_ros.corner_detection:main',
            'depth_node = opencv_ros.depth_camera:main',
            'hough = opencv_ros.hough_lines:main',
        ],
    },
)
