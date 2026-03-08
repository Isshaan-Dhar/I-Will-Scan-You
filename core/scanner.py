import socket
import threading
from queue import Queue

class MultiThreadedScanner:
    def __init__(self, target, thread_count=100):
        self.target = target
        self.target_ip = socket.gethostbyname(self.target)
        self.thread_count = thread_count
        self.queue = Queue()
        self.open_ports = []

    def worker(self):
        while not self.queue.empty():
            port = self.queue.get()
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.5)
            if sock.connect_ex((self.target_ip, port)) == 0:
                self.open_ports.append(port)
            sock.close()
            self.queue.task_done()

    def run(self, port_range):
        for port in port_range:
            self.queue.put(port)
        for _ in range(self.thread_count):
            t = threading.Thread(target=self.worker, daemon=True)
            t.start()
        self.queue.join()

        return sorted(self.open_ports)
