import os
import pickle
import socket
import time


def _pickle_allowed():
    """Return True if insecure pickle network transport is allowed.

    SECURITY: Unpickling network data is dangerous. Kept for compatibility.
    Set CHESS_ALLOW_PICKLE=0 to refuse to unpickle and fail fast.
    """
    return os.getenv("CHESS_ALLOW_PICKLE", "1") not in {"0", "false", "False"}


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "localhost"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.board = self.connect()
        if not _pickle_allowed():
            raise RuntimeError(
                "Insecure pickle transport disabled (set CHESS_ALLOW_PICKLE=1 to enable)."
            )
        self.board = pickle.loads(self.board)

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(4096 * 8)

    def disconnect(self):
        self.client.close()

    def send(self, data, pick=False):
        """
        :param data: str
        :return: str
        """
        start_time = time.time()
        while time.time() - start_time < 5:
            try:
                if pick:
                    self.client.send(pickle.dumps(data))
                else:
                    self.client.send(str.encode(data))
                reply = self.client.recv(4096 * 8)
                try:
                    if not _pickle_allowed():
                        # If disabled mid-run, keep returning raw bytes.
                        break
                    reply = pickle.loads(reply)
                    break
                except (pickle.UnpicklingError, EOFError, ValueError) as e:
                    print(e)

            except socket.error as e:
                print(e)

        return reply
