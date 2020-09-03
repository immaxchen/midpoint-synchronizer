from setuptools import setup

setup(
    name='xsync',
    version='0.0.1',
    py_modules=['xsync'],
    python_requires='>=3.2',
    entry_points={
        "console_scripts": [
            "xsync = xsync:main",
        ],
    },
)

