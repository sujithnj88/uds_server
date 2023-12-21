from threading import Event, Thread
from typing import Any, Literal

import logging
import time


class UdsServer(Thread):
    protocol: Literal["CAN_TP"]
    timeout_s: float = 0.150

    def __init__(
            self,
            ecu_name: str = "Default",
            network_configuration: Any = None,
            protocol: Literal["CAN_TP"] = None,
            timeout_s: float = 0.150,
            worker_process: int = 4,
    ):
        self.ecu_name = ecu_name
        self.network_configuration = network_configuration
        self.protocol = protocol
        self.timeout_s = timeout_s
        self.worker_process = worker_process

        self.thread_event = Event()
        self.transport_handler = None

        super().__init__()
        self.daemon = True

        logging.basicConfig(
            format="%(levelname)s  ::  %(asctime)s %(message)s",
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.DEBUG
        )

    def run(self):
        """
        Code for process start here.
        :return: None
        """
        self.thread_event.set()
        logging.info("Start UDS Server Thread...")

        while self.thread_event.is_set():
            # self.transport_handler.read_periodic()
            time.sleep(0.005)  # Sleeping 5 ms to avoid CPU hogging.

    def stop(self):
        """
        Blocking call responsible for clearing the active `thread_event` object and wait for thread termination.
        :return: None
        """
        logging.info("Stopping UDS Server thread...")
        self.thread_event.clear()
        self.join(timeout=self.timeout_s)
        logging.info("Stopped UDS Server thread successfully...")
