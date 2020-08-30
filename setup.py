from setuptools import setup

setup(
    name='msync',
    version='0.0.1',
    py_modules=['msync'],
    python_requires='>=3.2',
    entry_points={
        "console_scripts": [
            "msync = msync:main",
        ],
    },
)

