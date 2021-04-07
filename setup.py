import setuptools
setuptools.setup(
    name='obsidian_lab',
    version='0.2',    
    author='Cristian Vasquez',
    description='Obsidian lab app',
    url='https://github.com/cristianvasquez/obsidian-lab-py',    
    project_urls={
        "Bug Tracker":"https://github.com/cristianvasquez/obsidian-lab-py/issues",
    },
    license='MIT',
    install_requires= [
                      'Flask',
                      'Flask-Cors',
                      'Flask-json-schema'
                      ],                  
    classifiers=[
        'Development Status :: Proof of concept',
        'Intended Audience :: Science/Research'
    ],
    entry_points={
        'console_scripts': [
            'obsidian-lab = obsidian_lab:main',
        ],
    },
    python_requires=">=3.6",
)