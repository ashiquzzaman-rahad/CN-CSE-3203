import time

class frame:
    header: str = "H"
    info: int
    tailer: str = "T"

class packet:
    data: int

s = frame()

def from_network_layer() -> int:
    data: int = int(input("Data packet from network layer:"))
    time.sleep(2)
    print("\n\nReceiving in data link layer....")
    time.sleep(2)

    print("|NETWORK_LAYER|", end="")
    for i in range(5):
        print(" -> ", end="")
        time.sleep(0.5)
    print("|DATA_LINK_LAYER|")    

    print(f"Data packet {data} is received from network layer...")
    return data

def to_physical_layer(s: frame) -> None:
    time.sleep(2)
    print("\n\nSending to physical layer....")
    time.sleep(2)

    print("|DATA_LINK_LAYER|", end="")
    for i in range(5):
        print(" -> ", end="")
        time.sleep(0.5)
    print("|PHYSICAL_LAYER|")  

    print(f"Data frame {s.header}{s.info}{s.tailer} sent to physical layer...")
    


def from_physical_layer() -> frame:
    time.sleep(2)
    print("\n\nReceiving from physical layer....")
    time.sleep(2)

    print("|PHYSICAL_LAYER|", end="")
    for i in range(5):
        print(" -> ", end="")
        time.sleep(0.5)
    print("|DATA_LINK_LAYER|")  

    print(f"Data frame {s.header}{s.info}{s.tailer} received from physical layer...")
    return s


def to_network_layer(info: int) -> None:
    time.sleep(2)
    print("\n\nSending to network layer...")
    time.sleep(2)

    print("|DATA_LINK_LAYER|", end="")
    for i in range(5):
        print(" -> ", end="")
        time.sleep(0.5)
    print("|NETWORK_LAYER|") 

    print(f"Data packet {info} sent to network layer...\n\n")


def sender1():
    buffer = packet()

    # for i in range(10):
    buffer.data = from_network_layer()
    s.info = buffer.data
    to_physical_layer(s)


def receiver1():
    r = frame()

    # for i in range(10):
    r = from_physical_layer()
    to_network_layer(r.info)


def main():
    for i in range(1):
        sender1()
        receiver1()


if __name__ == "__main__":
    main()