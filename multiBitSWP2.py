import time
import random

class frame:
    header: str = 'H'
    info: list = []
    tailer: str = "T"

class packet:
    data: int

WINDOW_SIZE: int = 3
DATA_LEN: int = 6

def from_network_layer():
    DATA: list = []
    print("Data packet from network layer:")
    for i in range(DATA_LEN):
        p = packet()
        # p.data = random.choice(['0000','0001','0010','0011','0100','0101'])
        p.data = random.choice(['A','B','C','D','E','F'])
        DATA.append(p.data)
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


def init_sender(window: list):
    i = 0
    for w in window:
        s = frame()
        s.info = f"{i}{w}"
        to_physical_layer(s)
        wait_for_ack(s)
        i += 1
    

def init_receiver(r: frame):
    from_physical_layer(r)
    send_ack(r)



def sender2(ack: frame, s: frame):
    received_ack(ack)
    to_physical_layer(s)
    wait_for_ack(s)

def receiver2(s: frame):
    send_ack(s)


def main():
    print(f"{WINDOW_SIZE}Bit Sliding Window Protocol Initiated!\n")
    Data_transmit: list = from_network_layer()
    window: list = []
    frame_to_send: int = 0
    for i in range(frame_to_send, frame_to_send + WINDOW_SIZE):
        window.append(Data_transmit[i])
    init_sender(window)

    for i in range(WINDOW_SIZE ,len(Data_transmit)):
        r = frame()
        r.info = f"{i-WINDOW_SIZE}{Data_transmit[i-WINDOW_SIZE]}"
        init_receiver(r)
        s = frame()
        s.info = f"{i}{Data_transmit[i]}"
        sender2(r, s)

    for i in range(len(Data_transmit) - WINDOW_SIZE ,len(Data_transmit)):
        r = frame()
        r.info = f"{i}{Data_transmit[i]}"
        receiver2(r)

    print("Transmission Completed!")
if __name__ == "__main__":
    main()