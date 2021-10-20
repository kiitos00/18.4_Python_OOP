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
    def __init__(self, start=100):
        self.start = self.nextSerial = start

    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.nextSerial}>"

    def generate(self):
        self.nextSerial += 1
        return self.nextSerial - 1
    
    def reset(self): 
        self.nextSerial = self.start

