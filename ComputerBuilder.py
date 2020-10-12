from Computer import Computer
import uuid


class ComputerBuilder:

    def __init__(self):
        self.computer = Computer(uuid.uuid1())

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model
