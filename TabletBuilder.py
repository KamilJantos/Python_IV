from Tablet import Tablet
import uuid


class TabletBuilder:
    def __init__(self):
        self.tablet = Tablet(uuid.uuid1())  # Wykorzystanie roznych nr seryjnych

    def configure_size(self, amount):
        self.tablet.size = amount

    def configure_memory(self, amount):
        self.tablet.memory = amount

    def configure_hdd(self, amount):
        self.tablet.hdd = amount

    def configure_gpu(self, gpu_model):
        self.tablet.gpu = gpu_model
