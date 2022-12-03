import setuptools
with open("README.md", "r") as fh:
   long_description = fh.read()
setuptools.setup(
   name='python-vscode-flask-tutorial',
   version='0.0.1',
   author="alex carvalho",
   author_email="alex.carvalho.data@gmail.com",
   description="The best python package in the world",
   long_description=long_description,
   long_description_content_type="text/markdown",
   url="https://github.com/alex-carvalho-data/python-sample-vscode-flask-tutorial",
   packages=["python-vscode-flask"] or setuptools.find_packages(),
   install_requires=["flask"],
   classifiers=[
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
   ],
)
