#!/usr/bin/python3
"""
This module demonstrates the use of mixins in Python
to build a Dragon class that can swim, fly, and roar
by combining small, focused behaviors.
"""
class SwimMixin:
    def swim(self):
        """Prints a message indicating the creature is swimming."""
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        """Prints a message indicating the creature is flying."""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        """Prints a message indicating the dragon is roaring."""
        print("The dragon roars!")
