from setuptools import find_packages, setup
from test_project import __version__

PACKAGE_REQUIREMENTS = ["pyyaml"]

LOCAL_REQUIREMENTS = [
    "pyspark==3.2.1",
    "delta-spark==1.1.0",
    "scikit-learn",
    "pandas",
    "mlflow",
]

TEST_REQUIREMENTS = [
    # development & testing tools
    "pytest",
    "coverage[toml]",
    "pytest-cov",
    "dbx>=0.8"
]

setup(
    name="test_project",
    packages=find_packages(exclude=["tests", "tests.*"]),
    setup_requires=["setuptools", "wheel"],
    install_requires=PACKAGE_REQUIREMENTS,
    extra_require={
        "local": LOCAL_REQUIREMENTS,
        "test": TEST_REQUIREMENTS,
    },
    entry_points={
        "console_scripts": [
            "bricks = test_project.tasks.dbx-demo-job:entrypoint"
        ]
    },
    version=__version__,
    description="",
    author="",
)