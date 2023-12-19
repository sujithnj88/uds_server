from can import Bus


class CanTp:
    def __init__(self, network_config: dict):
        self.can_bus = Bus(**network_config)

    def read_periodic(self):
        pass
