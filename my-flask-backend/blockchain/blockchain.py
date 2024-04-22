import json
from web3 import Web3, HTTPProvider
import json
import os
import base64
from datetime import datetime

def print_blockchain(blockchain):
    # data={}
    # for block in blockchain:
    #     print(block)
    #     print(block[3])
    #     hash = base64.b64encode(block[3]).decode('utf-8')
    #     string_block = [base64.b64encode(item).decode('utf-8') if isinstance(item, bytes) else item for item in block]
    #     data[hash] = string_block
    #     with open('.\\bcdata.json', 'w') as f:
    #         json.dump(data, f)
    data = {}
    for block in blockchain:
        print(block)
        print(block.number)
        # print(block[3])
        # hash = base64.b64encode(block[3]).decode('utf-8')
        # string_block = [base64.b64encode(item).decode('utf-8') if isinstance(item, bytes) else item for item in block]
        # data[hash] = string_block
        
        # Get the latest block
        latest_block = web3.eth.get_block('latest')

        # Print the block number and hash
        print(f"Block Number: {latest_block.number}")
        print(f"Block Hash: {latest_block.hash}")
        print(f"Block time stamp: {datetime.fromtimestamp(latest_block.timestamp)}")

    with open('.\\bcdata.json', 'w') as f:
        json.dump(data, f)


# Ganache CLI
# truffle development blockchain address
blockchain_address = 'http://localhost:9545'
 
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address)) 

# print('*********************************')

web3.eth.defaultAccount = web3.eth.accounts[0]


compiled_contract_path = 'build\\contracts\\gfg.json'
deployed_contract_address = '0x80261cD982328aF68e7dB8409270F2E6E902eb1B'



# load contract info as JSON
with open(compiled_contract_path) as file:
    contract_json = json.load(file)  
     
    # fetch contract's abi - necessary to call its functions
    contract_abi = contract_json['abi']
 

contract = web3.eth.contract(
    address = deployed_contract_address, abi = contract_abi)
print(contract)
blockchain=contract.functions.getBlockchain().call()

print('*********************************')
print("current blockchain : ")
if len(blockchain)==0:
    print("blockchain empty")
else:
    print_blockchain(blockchain)
print('*********************************')

# flag = 1

while True:
    if True:
    # if os.path.exists('.\\formdata.json'):
    #     print("file exists")
    #     f=open('.\\formdata.json','r')
    #     descr=f.readline()
    #     print(descr)
    #     print("hello")
    #     prev_addr=descr
    #     product_id=descr
        balance = web3.eth.get_balance(web3.eth.accounts[0])
        print("Balance before transaction:", balance)
        descr=input("description : ")
        prev_addr = input("enter the previous hash of blocks  used : (type 0 if no previous hash)")
        if prev_addr == '0':
            prev_addr = []
        else:
            prev_addr = prev_addr.split(" ")
            # prev_addr = [Web3.to_checksum_address(bytes.fromhex(addr).hex()) for addr in prev_addr.split(" ")]
            # prev_addr = [prev_addr.encode('utf-8').hex()]
        # prev_addr = [item.encode('utf-8') for item in prev_addr]
        # prev_addr_input = input("enter the previous hash of blocks used (type 0 if no previous hash): ")
        # prev_addr = [] if prev_addr_input == '0' else [prev_addr_input]
        product_id = input("enter the product id: ")
        # print(prev_addr)
        # product_id = input("enter the  product id : ")
        # prev_addr_hex = [Web3.to_checksum_address(addr) for addr in prev_addr]
        trans = contract.functions.addBlock(descr,prev_addr,product_id).transact({'from':web3.eth.accounts[0]})
        
        receipt = web3.eth.wait_for_transaction_receipt(trans)

        gas_cost = receipt['gasUsed']
        print("Gas used:", gas_cost)
        balance = web3.eth.get_balance(web3.eth.accounts[0])
        print("Balance after transaction:", balance)

    # Get balance after transaction

        blockchain=contract.functions.getBlockchain().call()   
        print('*********************************')

        print("updated blockchain : ")
        print_blockchain(blockchain)
        print('*********************************')



        
        # os.remove('.\\formdata.json')