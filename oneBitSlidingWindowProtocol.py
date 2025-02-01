import time

class frame:
    header: str = 'H'
    info: list = []
    tailer: str = "T"

class packet:
    data: list = []

s = frame()
r = frame()
WINDOW_SIZE: int = 1
WINDOW: list = []

def from_network_layer() -> list:
    DATA: list = []
    # WINDOW = []
    print("Data packet from network layer:")
    for w in range(WINDOW_SIZE):
        for i in range(4):
            d: int = int(input())
            DATA.append(d)
        WINDOW.append(DATA)
    # print(WINDOW[0])
    print(f"Data packet(s) {WINDOW} is received from network layer...")
    return WINDOW


def to_physical_layer(s: frame) -> None:
    time.sleep(2)
    print("\n\nSending to physical layer....")
    time.sleep(2)
    print(f"Data frame {s.header}{s.info}{s.tailer} sent to physical layer!")
    

def from_physical_layer() -> frame:
    time.sleep(2)
    print("\n\nReceiving from physical layer....")
    time.sleep(2)
    print(f"Data frame {s.header}{s.info}{s.tailer} received from physical layer...")
    return s


def to_network_layer(info: int) -> None:
    time.sleep(2)
    print("\n\nSending to network layer...")
    time.sleep(2) 
    print(f"Data packet {info} sent to network layer...")



def sender1(next_frame_to_send: int):
    window = from_network_layer()
    # send: int = 0
    buffer = packet()
    # if send <= len(window) - 1:
    #     send += 1
    # else:
    #     send = 0
    buffer.data = window[next_frame_to_send]
    s.info = buffer.data

    print(f"Data frame of squence {next_frame_to_send} is being sent to receiver...")
    print("|SENDER|", end="")
    for i in range(5):
        print(" -> ", end="")
        time.sleep(0.5)
    print("|RECEIVER|")
    print(f"Data frame of squence {next_frame_to_send}: {s.header}{s.info}{s.tailer} - sent to receiver!")
    print(f"Start timer. Waiting for acknowledgement of data frame of squence {next_frame_to_send}...")

    to_physical_layer(s)


def sender2(next_frame_to_send) -> int:
    a = from_physical_layer()
    if next_frame_to_send in s.info:
        print(f"Acknowledge of data frame of squence {next_frame_to_send}: {a.header}{a.info}{a.tailer} - received from receiver!")
        print('Timer reset.')
        next_frame_to_send += 1

    return next_frame_to_send
    

def receiver1(frame_expected: int):
    print(f"Receiver is ready. Waiting for data frame of squence {frame_expected}...")


def receiver2(frame_expected) -> int:
    r = from_physical_layer()
    frame_recieved: int = frame_expected
    print(f"Data frame of squence {frame_recieved}: {s.header}{s.info}{s.tailer} - received from sender!")

    frame_expected += 1
    s.info = [frame_recieved, frame_expected]

    print(f"Acknowledgement of data frame of squence {frame_recieved} is being sent to sender...")
    print("|RECEIVER|", end="")
    for i in range(5):
        print(" -> ", end="")
        time.sleep(0.5)
    print("|SENDER|")
    print(f"Acknowledge of data frame of squence {frame_recieved}: {s.header}{s.info}{s.tailer} - sent to sender!")
    to_physical_layer(s)
    print(f"Start timer. Waiting for data frame of sequence {frame_expected}...")

    to_network_layer(r.info)
    return frame_expected


def main():
    print(f"{WINDOW_SIZE}-bit window initialized...\n\n")
    next_frame_to_send = 0
    frame_expected = 0
    for i in range(3):
        receiver1(frame_expected)
        sender1(next_frame_to_send)
        frame_expected = receiver2(frame_expected)
        next_frame_to_send = sender2(next_frame_to_send)


if __name__ == "__main__":
    main()