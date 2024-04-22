from web3 import Web3, HTTPProvider
from datetime import datetime
import json
import os 

#global variables
ports_in_use = [9545]
Web3_instances = []
contracts=[]

def print_balance(w3):
    balance = w3.eth.get_balance(w3.eth.accounts[0])
    print(f"Balance: {balance}")

def add_block(w3,index):
    contract = contracts[index]
    f=open('.\\formdata.json','r')
    descr=f.readline()
    print(descr)
    prev_addr=descr
    product_id=descr
    # os.remove('.\\formdata.json')



    #descr=input("description : ")
    #prev_addr = input("enter the previously used block number : (type - if no previous block)")
    #if prev_addr == '-':
    #    prev_addr = []
    #else:
    #    prev_addr = list(map(int,prev_addr.split(" ")))
    #product_id = input("enter the product id: ")

    trans = contract.functions.addBlock(descr,prev_addr,product_id).transact({'from':w3.eth.accounts[0]})
    receipt = w3.eth.wait_for_transaction_receipt(trans)
    gas_cost = receipt['gasUsed']
    print("Gas used:", gas_cost)


#function to start a node
def start_node(port):
    #create a new instance of Web3
    w3 = Web3(HTTPProvider(f'http://localhost:{port}'))
    w3.eth.defaultAccount = w3.eth.accounts[0]
    compiled_contract_path = 'build\\contracts\\gfg.json'
    deployed_contract_address = '0x80261cD982328aF68e7dB8409270F2E6E902eb1B'
    
    # load contract info as JSON
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  
        
        # fetch contract's abi - necessary to call its functions
        contract_abi = contract_json['abi']
    contract = w3.eth.contract(address = deployed_contract_address, abi = contract_abi)
    # print(contract)
    contracts.append(contract)
    ports_in_use.append(port)
    Web3_instances.append(w3)

#function to print the blockchain
def print_blockchain(blockchain,w3):
    data = {}
    
    for i in range(len(blockchain)):
        block = w3.eth.get_block(i)
        n=block["number"]
        data[n] = blockchain[i]
        # print(block)
        print(f"Block Number: {block.number}")
        print(f"Block Hash: {block.hash}")
        print(f"Block time stamp: {datetime.fromtimestamp(block.timestamp)}")
        print("Block Data: ",blockchain[i])
        # block_data = blockchain[i]
        # if len(block_data[1])!=0:
          #  for i in range(len(block_data[1])):
                # print(f"Product ID: {block_data[1][i]}")
               # child_block = w3.eth.get_block(block_data[1][i])

    with open('.\\bcdata.json', 'w') as f:
        json.dump(data, f)



#main function
start_node(9545)
while True:
    #("MENU")
    #print("1. Get block details")
    #print("2. Get blockchain details")
    #print("3. Add a block")
    # print("4. Add a node")  
    #a = input("Enter your choice: ")
    if os.path.exists('.\\buttondata.json'):
        f=open('buttondata.json','r')
        data = json.load(f)
        a = data["buttonname"]
       # a=l["buttonname"]
        print(a)
        if a == 'displayblock':
            print("Get block details")
            block_number = int(input("Enter block number: "))
            #port = input("Enter port number of node: ")
            port=9545
            # if port in ports_in_use:
            index = ports_in_use.index(port)
            
            #     # continue with the rest of the code
            # else:
            #     print("Port not found in ports_in_use")
            w3 = Web3_instances[index]
            block = w3.eth.get_block(block_number)
            print(f"Block Number: {block.number}")
            print(f"Block Hash: {block.hash}")
            print(f"Block time stamp: {datetime.fromtimestamp(block.timestamp)}")
        
        elif a == 'display':
            print("Get blockchain details")
            #port = input("Enter port number of node: ")
            port = 9545
            # if port in ports_in_use:
            index = ports_in_use.index(port)
            print(index)
                # continue with the rest of the code
            # else:
                # print("Port not found in ports_in_use")
            w3 = Web3_instances[index]
            contract = contracts[index]
            blockchain = contract.functions.getBlockchain().call()
            print("current blockchain : ")
            if len(blockchain)==0:
                print("blockchain empty")
            else:
                print_blockchain(blockchain,w3)

        elif a == 'add':
            
            print("Add a block")
            # block_data = input("Enter block data: ")
            # port = input("Enter port number of node: ")
            port = 9545
            # if port in ports_in_use:
            index = ports_in_use.index(port)
            #     # continue with the rest of the code
            # else:
            #     print("Port not found in ports_in_use")
            w3 = Web3_instances[index]
            print('balance before adding block')
            print_balance(w3)
            add_block(w3,index)
            print('balance after adding block')
            print_balance(w3)


    #elif a == '4':
     #   print("Add a node")
      #  port = input("Enter port number of new node: ")
       # start_node(port)

    else:
        print("Invalid choice")
    os.remove('.\\buttondata.json')
    
 