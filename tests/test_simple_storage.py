from brownie import SimpleStorage, accounts


def test_deploy():
    # arrange
    account = accounts[0]
    # act
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    # assert
    assert stored_value == 0


def test_store_value():
    # arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # act
    simple_storage.store(15, {"from": account})
    updated_value = simple_storage.retrieve()
    # assert
    assert updated_value == 15
