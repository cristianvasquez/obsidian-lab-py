import setuptools
import pathlib


# The text of the README file
readme_txt = (pathlib.Path(__file__).parent / "README.md").read_text()

setuptools.setup(
    name='obsidian_lab',
    version='0.2.4',    
    author='Cristian Vasquez',
    description='Obsidian lab app',
    long_description = readme_txt,
    long_description_content_type="text/markdown",
    url='https://github.com/cristianvasquez/obsidian-lab-py',    
    project_urls={
        "Bug Tracker":"https://github.com/cristianvasquez/obsidian-lab-py/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    license='MIT',
    install_requires= [
                      'Flask',
                      'Flask-Cors',
                      'Flask-json-schema'
                      ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Environment :: Plugins',
        'Intended Audience :: Science/Research'
    ],
    entry_points={
        'console_scripts': [
            'obsidian-lab = obsidian_lab:main',
        ],
    },
    python_requires=">=3.6",
)