from setuptools import find_packages, setup

package_name = 'learning_tf2_py'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # 런치파일 추가 
        ('share/' + package_name + '/launch', ['launch/tf2_learning.launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ggh',
    maintainer_email='ggh@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'static_turtle_tf2_broadcaster = learning_tf2_py.static_turtle_tf2_broadcaster:main',
            'turtle_tf2_broadcaster = learning_tf2_py.turtle_tf2_broadcaster:main',
            'turtle_tf2_listener = learning_tf2_py.turtle_tf2_listener:main',
        ],
    },
)
