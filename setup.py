from setuptools import setup, find_packages

setup(
   name="scikit-flowers",
   version="0.0.1",
   description='Scikit-Flowers or skflowers is a framework for explore data streaming and using scikit-learn compatible model-based in decision trees.',
   url='https://github.com/darosantos/scikit-flowers',
   author='Danilo R Santos',
   author_email='danilo.santosrs /|at|\ hotmail.com',
   license='GPL',
   platforms='any',
   keywords='machine-learning data-mining python3 scikit-learn ensemble-learning classification-model decision-trees',
   packages=find_packages(exclude=("research",".git")),
   include_package_data=True,
)