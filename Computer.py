class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None  # in gigabytes
        self.hdd = None  # in gigabytes
        self.gpu = None

    def __str__(self):
        info = (f'Serial Number: {self.serial}',
                f'Memory: {self.memory}GB',
                f'Hard Disk: {self.hdd}GB',
                f'Graphics Card: {self.gpu}')
        return '\n'.join(info)
