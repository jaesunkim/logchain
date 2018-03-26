import json
from smartcontract import contractmanager


def verify_tx_list(tx_list):
    contract_manager = contractmanager.ContractManager()
    for transaction in tx_list:
        data = json.dumps(transaction, indent=4, default=lambda o: o.__dict__, sort_keys=True)
        if data['type'] == 'CT':
            contract_manager.deploy_contract(data['extra_data']['contract_body'], data['extra_data']['contract_args'])

        elif data['type'] == 'RT':
            contract_manager.execute_contract(data['extra_data']['contract_addr'], data['extra_data']['contract_function'], data['extra_data']['contract_args'])


def verify(block):
    contract_manager = contractmanager.ContractManager()
    for transaction in block.tx_list:
        data = json.dumps(transaction, indent=4, default=lambda o: o.__dict__, sort_keys=True)
        if data['type'] == 'CT':
            contract_manager.deploy_contract(data['extra_data']['contract_body'], data['extra_data']['contract_args'])

        elif data['type'] == 'RT':
            contract_manager.execute_contract(data['extra_data']['contract_addr'], data['extra_data']['contract_function'], data['extra_data']['contract_args'])