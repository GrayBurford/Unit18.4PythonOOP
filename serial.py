"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """
        Defines a serial #'s start value from user input
        """
        self.start = start
        self.next_val = start
    
    def __repr__(self):
        """
        Representation of this class
        """
        return f'Serial Generator with start #: {self.start} and next #: {self.next_val + 1}'

    def generate(self):
        """
        Increments serial # by 1, and returns next serial # value
        """
        self.next_val += 1
        return self.next_val - 1

    def reset(self):
        """
        Resets serial # value to default start value
        """
        self.next_val = self.start
