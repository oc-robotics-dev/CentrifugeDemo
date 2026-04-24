from setuptools import find_packages, setup

package_name = 'centrifuge_control'

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
    maintainer='ocr',
    maintainer_email='ocr@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'keyboard_centrifuge = centrifuge_control.keyboard_centrifuge:main',
            'serial_bridge = centrifuge_control.serial_bridge:main',
        ],
    },
)
