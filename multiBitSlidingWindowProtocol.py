import time
import random

class frame:
    header: str = 'H'
    info: list = []
    tailer: str = "T"

class packet:
    data: list = []

s = frame()
r = frame()
WINDOW_SIZE: int = 2
WINDOW: list = []
SENT_WINDOW: list = []

def from_network_layer() -> list:
    DATA: list = []
    print("Data packet from network layer:")
    for i in range(10):
        d: int = random.choice([0,1,2,3,4,5])
        DATA.append(d)
    print(f"Data packet(s) {DATA} is received from network layer...")
    return DATA


def to_physical_layer(sent: frame) -> None:
    time.sleep(2)
    print("\n\nSending to physical layer....")
    time.sleep(2)
    print(f"Data frame {sent.header}{sent.info}{sent.tailer} sent to physical layer!")
    

def from_physical_layer(SENT_WINDOW) -> list:
    received: list = SENT_WINDOW
    print(SENT_WINDOW)
    # time.sleep(2)
    # print("\n\nReceiving from physical layer....")
    for i in range(WINDOW_SIZE):
        time.sleep(2)
        r = frame()
        r = received[i]
        print(f"Data frame {r.header}{r.info}{r.tailer} receiving from physical layer...")

    return received


def to_network_layer(info: int) -> None:
    time.sleep(2)
    print("\n\nSending to network layer...")
    time.sleep(2) 
    print(f"Data packet {info} sent to network layer...")


def sender1(next_frame_to_send: int) -> list:
    buffer = packet()
    SENT_WINDOW = []
    for i in range(WINDOW_SIZE):
        buffer.data = WINDOW[i]
        s.info = buffer.data
        SENT_WINDOW.append(s)
        squence = next_frame_to_send + i
        print(f"Data frame of squence {squence} is being sent to receiver...")
        to_physical_layer(s)
        print("|SENDER|", end="")
        for i in range(5):
            print(" -> ", end="")
            time.sleep(0.5)
        print("|RECEIVER|")
        print(f"Data frame of squence {squence}: {s.header}{s.info}{s.tailer} - sent to receiver!")
        print(f"Start timer. Waiting for acknowledgement of data frame of squence {squence}...")

    return SENT_WINDOW


def sender2(next_frame_to_send) -> int:
    a = from_physical_layer()
    for i in range(WINDOW_SIZE):
        r = frame()
        r = a[i]
        print(f"Acknowledge of data frame of squence {next_frame_to_send+i}: {r.header}{r.info}{r.tailer} - received from receiver!")
        
    print('Timer reset.')
    next_frame_to_send += WINDOW_SIZE

    return next_frame_to_send
    

def receiver1(frame_expected: int):
    print(f"Receiver is ready.") 
    print("Waiting for data frame of squence ", end="")
    for i in range(WINDOW_SIZE):
        print(f"{frame_expected+i}", end=" ")
    print("\n")


def receiver2(frame_expected, received) -> int:
    # received = from_physical_layer()
    frame_recieved: int = frame_expected
    SENT_WINDOW = []
    for i in range(WINDOW_SIZE):
        s = received[i]
        print(f"Data frame of squence {frame_recieved+i}: {s.header}{s.info}{s.tailer} - received from sender!")
        ack = frame()
        ack.info = f"frame:{frame_recieved+i}"
        SENT_WINDOW.append(ack)
        print(f"Acknowledgement of data frame of squence {frame_recieved+i} is being sent to sender...")
        to_physical_layer(ack)

        print("|RECEIVER|", end="")
        for i in range(5):
            print(" -> ", end="")
            time.sleep(0.5)
        print("|SENDER|")

        print(f"Acknowledge of data frame of squence {frame_recieved+i}: {ack.header}{ack.info}{ack.tailer} - sent to sender!")
        

    frame_expected += WINDOW_SIZE
    
    for i in range(WINDOW_SIZE):
        r = frame()
        r = received[i]
        to_network_layer(r.info)
    # print(f"Start timer. Waiting for next data frame of sequence {frame_expected}...")
    return frame_expected


def main():
    print(f"{WINDOW_SIZE}-bit window initialized...\n\n")
    Data = from_network_layer()
    next_frame_to_send = 0
    frame_expected = 0
    for i in range(1):
        receiver1(frame_expected)

        for j in range(next_frame_to_send, next_frame_to_send+WINDOW_SIZE):
            WINDOW.append(Data[j])

        SENT_WINDOW = sender1(next_frame_to_send)
        received = from_physical_layer(SENT_WINDOW)

        frame_expected = receiver2(frame_expected, received)

        next_frame_to_send = sender2(next_frame_to_send)


if __name__ == "__main__":
    main()