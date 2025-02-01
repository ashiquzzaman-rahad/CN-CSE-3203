import time
import random

class frame:
    header: str = 'H'
    info: list = []
    tailer: str = "T"

class packet:
    data: list = []

WINDOW_SIZE: int = 3

def from_network_layer():
    DATA: list = []
    print("Data packet from network layer:")
    for i in range(6):
        d: int = random.choice(['0000','0001','0010','0011','0100','0101'])
        DATA.append(d)
    print(f"Data packet(s) {DATA} is received from network layer...\n")
    return DATA

def to_physical_layer(sent: frame):
    print(f"Data frame {sent.header}{sent.info}{sent.tailer} sent to physical layer!")

def wait_for_ack(sent: frame):
    print("|SENDER|", end="")
    for i in range(5):
        print(" -> ", end="")
        time.sleep(0.5)
    print("|RECEIVER|")
    print(f"Waiting for ack of {sent.header}{sent.info}{sent.tailer} from receiver...\n")

def from_physical_layer(received: frame):
    print(f"Data frame {received.header}{received.info}{received.tailer} received from sender!")


def send_ack(received: frame):
    print(f"Sending ack of {received.header}{received.info}{received.tailer} to sender...")
    print("|RECEIVER|", end="")
    for i in range(5):
        print(" -> ", end="")
        time.sleep(0.5)
    print("|SENDER|")
    print(f"Ack sent for data frame {received.header}{received.info}{received.tailer} to sender!\n")


def received_ack(sent: frame):
    print(f"Ack received for data frame {sent.header}{sent.info}{sent.tailer} from receiver!\n")


def sender(window: list):
    for w in window:
        s = frame()
        s.info = w
        to_physical_layer(s)
        wait_for_ack(s)
    

def receiver(window: list):
    for w in window:
        r = frame()
        r.info = w
        from_physical_layer(r)
        send_ack(r)

def sender2(window: list):
    for w in window:
        s = frame()
        s.info = w
        received_ack(s)


def main():
    Data_transmit: list = from_network_layer()
    frame_to_send: int = 0
    for term in range(2):
        window: list = []
        for i in range(frame_to_send, frame_to_send + WINDOW_SIZE):
            window.append(Data_transmit[i])
        frame_to_send += WINDOW_SIZE
        sender(window)
        receiver(window)
        sender2(window)
        



if __name__ == "__main__":
    main()