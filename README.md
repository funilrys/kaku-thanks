# Kaku `thanks.json`

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![GitHub release](https://img.shields.io/github/release/funilrys/kaku-thanks.svg)](https://github.com/funilrys/kaku-thanks/releases/tag/1.0.0)

> Generate the famous thanks.json of Kaku

## Features

- Generate thanks.json of Kaku

This repository also include the features of the following projects:

- [Fasternix Stratalorn](https://github.com/funilrys/Fasternix-Stratalorn) (Transifex Translators)
- [Obstructing Trio](https://github.com/funilrys/Obstructing-Trio) (GitHub Contributors)

--------------------------------------------------------------------------------

### Fasternix Stratalorn (Transifex Translators)

- Works with python3.x and python2.x
- Access Transifex project details
- Get list of translators and save the result into a JSON file
- Get list of translators and return the result in Python `dict` format
- Get list of translators and return the result in Python `list` format

### Obstructing Trio (GitHub Contributors)

- Works with Python 3.x and Python 2.x
- Access GitHub repository contributors list
- Get list of contributors username in JSON format
- Get list of contributors username in Python `dict` format
- Get list of contributors username in Python `list` format
- Exclude username from generated list

--------------------------------------------------------------------------------

## Installation

### From Github

```shell
$ git clone https://github.com/funilrys/kaku-thanks.git

# The following will install fasternix_stratalorn and obstructing_trio into
# your python environment
$ cd kaku-thanks && ./execute_me_first
```

## Help/usage

```shell
$ python thanks.py -h
usage: thanks.py [-h] [-o OUTPUT] username

Generate the famous thanks.json of Kaku. More
informations about Kaku at https://github.com/EragonJ/Kaku

positional arguments:
  username              Transifex username. Must be a maintainer of
                        Kaku Transifex project

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Define where thanks.json is gonna be
                        saved

Crafted with ♥ by Nissar Chababy (Funilrys)
```

## Examples of usage

### Common Usage

The following will simply generate `thanks.json` into our current location

```shell
# The username of a valid maintainer of the Transifex project is needed.
# Password is asked.
$ python thanks.py funilrys
```

### Different location

The following will simply generate `thanks.json` into the desired location

```shell
# The username of a valid maintainer of the Transifex project is needed.
# Password is asked.
$ python thanks.py funilrys -o ..

# Same for the following.
$ python thanks.py funilrys --output ..
```

--------------------------------------------------------------------------------

### Fasternix Stratalorn (Transifex Translators)

Please report [here](https://github.com/funilrys/Fasternix-Stratalorn#examples-of-usage) for more examples.

#### Common usage

The following will save the **list of translator** into `translators.json` in you **current location**.

```python
from fasternix_stratalorn import get

get('funilrys', 'desktop-app')
```

### Obstructing Trio (GitHub Contributors)

Please report [here](https://github.com/funilrys/Obstructing-Trio#examples-of-usage) for more examples.

#### Common usage

The following will save the **list of contributors** into `contributors.json` in you **current location**.

```python
#!/bin/env python
from obstructing_trio import get

get('EragonJ/Kaku')
```

--------------------------------------------------------------------------------

# How to contribute?

To contribute, you have to **send a new [Pull Request](https://github.com/funilrys/kaku-thanks/compare)** after you **[forked](https://github.com/funilrys/kaku-thanks/pulls#fork-destination-box)** and edited the script(s).

## :warning: WARNING :warning:

### DO NOT FORGET

- To sign your commit(s) with **"Signed-off by: FirstName LastName < email at service dot com >"** _and/or_ simply **sign your commit(s)** with **PGP** _(Please read more [here](https://github.com/blog/2144-gpg-signature-verification))_.
- All **contributions/modifications** must be done under **the `dev` or a new branch** if you plan to **send a new [Pull Request](https://github.com/funilrys/kaku-thanks/compare)**.
- :warning: Every **contributions/modifications** which are under **master** _(exception for minor changes)_ **will not be merged**. :warning:

--------------------------------------------------------------------------------

# License

```
MIT License

Copyright (c) 2017 Nissar Chababy <contact at funilrys dot com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
