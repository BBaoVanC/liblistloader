# liblistloader

[![Build Status](https://drone.bbaovanc.com/api/badges/bbaovanc/liblistloader/status.svg)](https://drone.bbaovanc.com/bbaovanc/liblistloader)

![PyPI](https://img.shields.io/pypi/v/liblistloader)
![PyPI - License](https://img.shields.io/pypi/l/liblistloader)

Library for loading word lists from files. Built for [libnamegen](https://git.bbaovanc.com/bbaovanc/libnamegen)

## Features

* Easy to use
* Imported as module
* Always tested before release
* Supports latest three versions of Python 3

---

## Included word lists

* `liblistloader.desiquintans_nounlist`: [The Great Noun List](http://www.desiquintans.com/nounlist) by desiquintans.com

---

## How to Install

Run the command `pip install liblistloader`. If you want to specify a specific Python version to use for pip, use a command such as `pip3` or `pip3.8`.

---

## Documentation

### API

To import a single list, type `import liblistloader.[word list]`. Then, you can get a list, each item being a word in the word list, by typing `liblistloader.[word list].words`.

WARNING! These lists are VERY long! For example, desiquintans_nounlist is 6,801 words long! Therefore, `liblistloader.desiquintans_nounlist.words` returns a list with 6,801 items in it. I would not recommend the following code for your sanity:

``` python
import liblistloader.desiquintans_nounlist

for word in liblistloader.desiquintans_nounlist.words:
    print(word)
```

Output (total 6,801 lines):

``` plaintext
ATM
CD
SUV
TV
aardvark
abacus
abbey
abbreviation
abdomen
...
```

---

Import all noun lists and pick a random word from a few:

``` python
import random
import liblistloader

print("desiquintans_nounlist: " + random.choice(liblistloader.desiquintans_nounlist.words))
```

Output (will vary because a random word is being picked):

``` plaintext
desiquintans_nounlist: velocity
```

---

## License

_liblistloader_ is licensed under the GPLv3 license. For more information, please refer to [`LICENSE`](https://git.bbaovanc.com/bbaovanc/liblistloader/src/branch/master/LICENSE).
