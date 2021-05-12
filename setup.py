import setuptools

setuptools.setup(name='package_example',
                 version='0.1',
                 description='Test',
                 url='https://github.com/Ununnilium/test_package',
                 packages=['package_example'],
                 python_requires='>=3.6',
                 install_requires=[
                     'pandas', 'tqdm'],
                 entry_points={'console_scripts': ['test-script=package_example.test_file:main']},
                 )
