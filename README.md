# mercury-db


![GitHub followers](https://img.shields.io/github/followers/smv1999?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/smv1999/mercury-db?style=for-the-badge)
![GitHub Repo stars](https://img.shields.io/github/stars/smv1999/mercury-db?style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/smv1999/mercury-db?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/smv1999/mercury-db?color=blue&style=for-the-badge)
![PyPI](https://img.shields.io/pypi/v/mercury-db?color=blue&style=for-the-badge)


This is a File Based Key-Value Datastore that supports basic CRUD (Create, Read, Update, Delete) operations developed using `Python`.

The data store will support the following functional requirements:

1. A new key-value pair can be added to the data store using the Create operation. The key is always a string - capped at 32chars. The value is always a JSON object-capped at
   16KB.
1. A Read operation on a key can be performed by providing the key, and receiving the
   value in response, as a JSON object.
1. A Delete operation can be performed by providing the key.
1. Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.

The data store will also support the following non-functional requirements:

1. The size of the file storing data must never exceed 1GB.
1. More than one client process cannot be allowed to use the same file as a data store at any given time
1. A client process is allowed to access the data store using multiple threads, if it desires to The data store must therefore be thread-safe.


## Overview

The application has been developed as a library so that users can just import it and create an instance of the class and work with the data store by invoking relevant methods. The application satisfies both the **functional and non-functional requirements mentioned above**.

## File Structure

- `src/mercury_db/datastore.py` - The library that contains the methods for performing CRUD Operations.
- `setup.py` 

## Installation

```
pip install mercury-db
```

## Usage

Consider the following examples:

```python
from src.mercury_db.datastore import *

ds = DataStore()
ds.create('myname', 'Vaidhyanathan', 60)
print(ds.read('myname'))
ds.create('New Delhi', 'India Gate')
ds.delete('myname')
print(ds.read('New Delhi'))
print(ds.read('name'))

```

## Development Environment

- OS: Linux (Ubuntu) - Linux-5.11.0-41
- Language(s) used: Python

The application **doesn't have any OS specific dependencies and should run without any problems in Mac and Windows as well**.

## Bugs/Requests 

Please use the [GitHub issue tracker](https://github.com/smv1999/mercury-db/issues) to submit bugs or request features.

## License 

Copyright Vaidhyanathan S M, 2021

Distributed under the terms of the [MIT](https://github.com/smv1999/mercury-db/blob/main/LICENSE) license, py-dsa is free and open source software.

