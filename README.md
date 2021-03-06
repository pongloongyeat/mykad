# MyKad

A Python package to check if a MyKad number is valid and gets information such as the birthdate, state of birth and gender.

![screenshot](https://raw.githubusercontent.com/pongloongyeat/mykad/d05cabbde7bd13869c11fd192b81a1b1bbe5a754/images/mykad.png)

## The `MyKad` class

```python
from mykad.mykad import MyKad

mykad = MyKad(MYKAD_NUMBER)
```

The following methods are included in the `MyKad` class:

| Method                     | Comment                                                 |
|----------------------------|---------------------------------------------------------|
| `get_unformatted()`        | Gets the unformatted MyKad string.                      |
| `get_formatted()`          | Gets the formatted MyKad string.                        |
| `is_male()`                | Checks if the MyKad holder is a male.                   |
| `is_female()`              | Checks if the MyKad holder is a female.                 |

The following attributes are included in the `MyKad` class:

| Attribute                  | Comment                                                                  |
|----------------------------|--------------------------------------------------------------------------|
| `birthdate`                | Gets the datetime instance corresponding to the MyKad holder's birthdate.|
| `birth_year`               | Gets the birth year of the MyKad holder.                                 |
| `birth_month`              | Gets the birth month of the MyKad holder.                                |
| `day_of_birth`             | Gets the day of birth of the MyKad holder.                               |
| `birthplace`               | Gets the birthplace of the MyKad holder.                                 |
| `gender`                   | Gets the gender of the MyKad holder.                                     |

## Included utility functions

The following utility functions are included under `mykad.utils`:

| Utility                   | Comment                                                           |
|---------------------------|-------------------------------------------------------------------|
| `is_mykad_valid`          | Checks if a MyKad is valid.                                       |
| `get_birthplace`          | Quickly check the birthplace corresponding to a birthplace code.  |
| `get_state_abbreviation`  | Gets the state abbreviation                                       |
