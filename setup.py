import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

     name='qurry',

     version='0.0.2',

     scripts=['compile-qurry', 'quilarity', 'qurry-server'] ,

     author="Lucas Saldyt",

     author_email="lucassaldyt@gmail.com",

     description="A prototype quantum programming language",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/LSaldyt/qurry",

     # I manually typed these, but there must be a better way! TODO I guess.
     #packages=['qurry', 'qurry.library', 'qurry.compiler', 'qurry.constructs', 'qurry.datatypes', 'qurry.kernel', 'qurry.library', 'qurry.visualization'],
     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )
