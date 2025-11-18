from setuptools import find_packages, setup

package_name = 'first_package'

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
    maintainer='diogo',
    maintainer_email='dsouzalve@gmail.com',
    description='PrimeiroPackage',
    license='New license',
    
    
    
    extras_require={
        'test': [
            'pytest',
        ],
    },
    
    
    entry_points={
        'console_scripts': ['talker = first_package.publisher:main', 
        'listener = first_package.subscriber:main',
        ],                  #nome da pasta que esta, o nome do arquivo e o nome da função
    },
)
