from threading import Event, Thread
from typing import Any, Literal

import time


class UdsServer(Thread):
    protocol: Literal["CAN_TP"]
    timeout_s: float = 0.150

    def __init__(
            self,
            network_configuration: Any = None,
            protocol: Literal["CAN_TP", "DOIP"] = None,
            worker_process: int = 4,
            timeout_s: float = 0.150
    ):
        self.network_configuration = network_configuration
        self.protocol = protocol
        self.timeout_s = timeout_s
        self.worker_process = worker_process

        self.thread_event = Event()
        self.transport_handler = None

        super().__init__()
        self.daemon = True

    def run(self):
        """
        Code for process start here.
        :return: None
        """
        self.thread_event.set()

        while self.thread_event.is_set():
            self.transport_handler.read_periodic()
            time.sleep(0.005)  # Sleeping 5 ms to avoid CPU hogging.


x = UdsServer()
x.start()
