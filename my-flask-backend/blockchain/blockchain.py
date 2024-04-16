import json
from web3 import Web3, HTTPProvider
import json
import os

# truffle development blockchain address
blockchain_address = 'http://localhost:9545'
 
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address)) 
# print('*********************************')

web3.eth.defaultAccount = web3.eth.accounts[0]


compiled_contract_path = 'build/contracts/gfg.json'
deployed_contract_address = '0x80261cD982328aF68e7dB8409270F2E6E902eb1B'
 
# load contract info as JSON
with open(compiled_contract_path) as file:
    contract_json = json.load(file)  
     
    # fetch contract's abi - necessary to call its functions
    contract_abi = contract_json['abi']
 

contract = web3.eth.contract(
    address = deployed_contract_address, abi = contract_abi)

blockchain=contract.functions.getBlockchain().call()

print('*********************************')

print("current blockchain : ")
if len(blockchain)==0:
    print("blockchain empty")
else:
    data={}
    i=1
    for block in blockchain:
        print(block)
        data[i]=block
        i+=1
    # print(blockchain)
        # print(data)
    with open('.\\bcdata.json', 'w') as f:
        json.dump(data, f)
print('*********************************')

flag = 1
while flag:
    if os.path.exists('.\\formdata.json'):
        f=open('.\\formdata.json','r')
        descr=f.readline()
        prev_addr=descr
        product_id=descr
        # descr=input("description : ")
        # prev_addr = input("enter the previous hash of blocks  used : ")
        # product_id = input("enter the  product id : ")
        trans = contract.functions.addBlock(descr,prev_addr,product_id).transact({'from':web3.eth.accounts[0]})

        web3.eth.wait_for_transaction_receipt(trans)
        blockchain=contract.functions.getBlockchain().call()   
        print('*********************************')

        print("updated blockchain : ")

        data={}
        i=1
        for block in blockchain:
            print(block)
            data[i]=block
            i+=1

        with open('.\\bcdata.json', 'w') as f:
            json.dump(data, f)
        print('*********************************')
        
        os.remove('.\\formdata.json')
    # flag = int(input('proceed adding more ? if yes type 1 else type 0 : '))