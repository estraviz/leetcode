# Two Sum

## Description

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

* Given nums = [2, 7, 11, 15], target = 9, because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1]:

```python
two_sum([2, 7, 11, 15], 9) # should return: [0, 1]
```

## Note

As the solution has been provided, we may launch it from the terminal as follows:

```python
$ python two_sum.py "[2, 7, 11, 13, 11]" 22
[2, 4]
```

Tests are prepared to be executed with `pytest` just by doing:

```python
$ pytest -v
```

in this same directory.