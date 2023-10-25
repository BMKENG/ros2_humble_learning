from setuptools import setup

setup(
    name='py_pubsub',
    version='0.0.0',
    packages=['py_pubsub'],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Author Name',
    author_email='author@example.com',
    maintainer='Maintainer Name',
    maintainer_email='maintainer@example.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'Description of your Python package.'
    ),
    license='Apache License, Version 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_pubsub.publisher_member_function:main',
            'listener = py_pubsub.subscriber_member_function:main',
        ],
    },
)