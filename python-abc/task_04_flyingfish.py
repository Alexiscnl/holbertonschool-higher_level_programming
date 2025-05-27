#!/usr/bin/python3
"""
This module demonstrates multiple inheritance in Python using
a FlyingFish class that inherits from both Fish and Bird.
Each parent class defines behavior, and FlyingFish overrides it
to show combined functionality.
"""
class Fish:
    def swim(self):
        """Prints the swimming behavior of a fish."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of a fish."""
        print("The fish lives in water")

class Bird:
    def fly(self):
        """Prints the flying behavior of a bird."""
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat of a bird."""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    def fly(self):
        """Overrides Bird.fly with flying fish behavior."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides Fish.swim with flying fish behavior."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides both Fish and Bird habitat methods."""
        print("The flying fish lives both in water and the sky!")
