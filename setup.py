from setuptools import setup


with open("requirements.txt") as fp:
    install_requires = fp.read()


setup(
    name="defer.py",
    version="0.1.0",
    description="golang defer equivalent in python",
    url=f"https://github.com/loynoir/defer.py",
    author="loynoir",
    license="MIT",
    install_requires=install_requires,
    packages=["Defer"],
    entry_points={
        "console_scripts": [],
    },
    keywords=["defer"],
)
