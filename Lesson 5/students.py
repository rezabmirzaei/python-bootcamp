#!/usr/bin/env python
# coding: utf-8

# docstring
"""students.py - Manage list of students in class"""

# import statements
# import classes

# authorship info, copyrights, licences etc.
__author__ = "Reza"

names = ["Truls", "Niels", "Ipek", "Danyia", "Anders"]

def is_student_enrolled(name):
    return name in names

def uppercase_names():
    return list(map(lambda name : name.upper(), names))