# IT Utilities
A set of IT utilities to help my daily life as a programmer, and a system administrator.

## Getting Started

These instructions will get you a copy of the project and running on your local machine for development and testing purposes.

```bash

git clone https://github.com/kranz912/IT_Utilities.git

cd IT_Utilities

```


### Prerequisites
Python is required for some tools to work.

You can download and install python from:

[Python.org](https://www.python.org/)



[Pipenv](https://github.com/pypa/pipenv) is required to install the dependencies. It creates a virtual environment for you.

To install Pipenv:
```bash
pip install pipenv
```

### Installing
Run the following command to install all the dependencies.

```bash

pipenv install

```

#### Usage
In order to use you must be on pipenv shell.

Run the following command on your terminal.

```bash
pipenv shell
```



#### Converting CSV file to JSON file

A tool for converting a CSV file to JSON file


```bash
usage: CsvToJson.py [-h] <source> <destination>

A utility to convert csv file to json file

positional arguments:
  <source>       source csv file
  <destination>  destination json file

optional arguments:
  -h, --help     show this help message and exit
```

example:
```bash

python CsvToJson.py ../test.csv ../test.json

```

#### Zipping a directory
A tool for zipping a directory
```bash
usage: Zipdir.py [-h] <source> <destination>

a utility that will convert a directory into a ZipFile

positional arguments:
  <source>       source directory directory path
  <destination>  destination directory path

optional arguments:
  -h, --help     show this help message and exit

```

example:

```bash

#zipping the current directory
python Zipdir.py . ../test.zip


#zipping another directory

python Zipdir.py D:\example D:\example.zip

```
