import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='118A_quiz',
    version='0.0.1',
    author='Scott',
    author_email='yuy004@ucsd.edu',
    description='Display the quiz content',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Muls/toolbox',
    project_urls = {
        "Bug Tracker": "https://github.com/Muls/toolbox/issues"
    },
    license='MIT',
    packages=['118A_quiz'],
    install_requires=['requests'],
)