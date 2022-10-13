from brownie import SimpleStorage


def read_value():
    simple_storage = SimpleStorage[-1]
    retrieved_value = simple_storage.retrieve()
    print(f"retrieved_value: {retrieved_value}")


def main():
    read_value()
