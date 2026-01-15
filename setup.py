from setuptools import setup, find_packages

setup(
    name="backtest_engine",
    version="0.1",
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    install_requires=[
        # Add dependencies here (e.g., pandas, numpy, etc.)
    ],
)
