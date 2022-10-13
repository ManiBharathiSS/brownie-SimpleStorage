from brownie import SimpleStorage, config, network, accounts


def deploy():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(f"stored value: {stored_value}")
    tx = simple_storage.store(15, {"from": account})
    tx.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(f"updated stored value: {updated_stored_value}")


def get_account():
    if network.show_active == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy()
