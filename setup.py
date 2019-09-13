import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

     name='qurry',

     version='0.0',

     scripts=['compile', 'quilarity', 'server'] ,

     author="Lucas Saldyt",

     author_email="lucassaldyt@gmail.com",

     description="A prototype quantum programming language",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/LSaldyt/qurry",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: MIT License",

         "Operating System :: OS Independent",

     ],

 )
