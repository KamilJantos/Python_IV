from ComputerBuilder import ComputerBuilder
from TabletBuilder import TabletBuilder


class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu):
        self.builder = ComputerBuilder()
        self.builder.configure_memory(memory)
        self.builder.configure_hdd(hdd)
        self.builder.configure_gpu(gpu)

    def construct_tablet(self, size, memory, hdd, gpu):
        self.builder = TabletBuilder()
        self.builder.configure_size(size)
        self.builder.configure_memory(memory)
        self.builder.configure_hdd(hdd)
        self.builder.configure_gpu(gpu)

    @property
    def computer(self):
        return self.builder.computer

    @property
    def tablet(self):
        return self.builder.tablet


def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=500,
                                memory=8,
                                gpu='GeForce GTX 650 Ti')
    computer = engineer.computer

    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=256,
                                memory=16,
                                gpu='GeForce GTX 650 Ti')
    computer1 = engineer.computer

    engineer.construct_tablet(size=23,
                              memory=1,
                              gpu='ATM',
                              hdd=49)
    tablet = engineer.tablet
    print("\nCOMPUTER:\n")
    print(computer)
    print("\nTABLET:\n")
    print(tablet)
    print("\nCOMPUTER_1\n")
    print(computer1)


if __name__ == '__main__':
    main()
