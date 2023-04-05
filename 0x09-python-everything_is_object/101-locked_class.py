#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Does not allow the uset to instantiate new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
