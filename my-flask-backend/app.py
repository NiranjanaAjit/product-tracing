from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from web3 import Web3, HTTPProvider
from datetime import datetime


#global variables
ports_in_use = [9545,9090]
Web3_instances = []
contracts=[]
app = Flask(__name__)
CORS(app, origins="*")

def print_balance(w3):
    balance = w3.eth.get_balance(w3.eth.accounts[0])
    print(f"Balance: {balance}")

def add_block(w3,index):
    contract = contracts[index]
    f=open('blockchain\\formdata.json','r')
    data=json.load(f)
    descr = data['descr']
    p=data['prevAddr']
    if p=="":
        prev_addr = []
    else:
        prev_addr = list(map(int,p.split(" ")))
    product_id=data['productId']
    balance_before = w3.eth.get_balance(w3.eth.accounts[0])
    trans = contract.functions.addBlock(descr,prev_addr,product_id).transact({'from':w3.eth.accounts[0]})
    receipt = w3.eth.wait_for_transaction_receipt(trans)
    gas_cost = receipt['gasUsed']
    print("Gas used:", gas_cost)
    print("Transaction receipt:", receipt)

    receipt_data = {
        'balance-before': balance_before,
        'transaction_hash': receipt['transactionHash'].hex(),
        'gas_used': receipt['gasUsed'],
        'status': receipt['status'],
        'from': receipt['from'],
        'to': receipt['to'],
        
        # 'time_stamp' : datetime.fromtimestamp(receipt['timestamp']),
        'balance-after': w3.eth.get_balance(w3.eth.accounts[0])


    }

    with open('blockchain/receipt.json', 'w') as f:
        json.dump(receipt_data, f)



def start_node(port):
    #create a new instance of Web3
    w3 = Web3(HTTPProvider(f'http://localhost:{port}'))
    w3.eth.defaultAccount = w3.eth.accounts[0]
    compiled_contract_path = 'blockchain\\build\\contracts\\gfg.json'
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


@app.route('/api/searchwithpeoductid',methods = ['POST'])
def search_with_product_id():
    data = request.get_json()
    product_id = data.get('input')
    port = 9545
    index = ports_in_use.index(port)
    w3 = Web3_instances[index]

    f=open('blockchain/bcdata.json','r')
    data=json.load(f)
    found = False
    for i in data:
        if i['product_id']==product_id:  
            found = True
            block_data = i
            break

    if found:
        f2=open('blockchain/blockdata.json','w')
        json.dump(block_data,f2)
        return jsonify({'searched for product_id': product_id})
    else:
        block_data = {'message': 'product_id not found'}
        f2=open('blockchain/blockdata.json','w')
        json.dump(block_data,f2)
        return jsonify({'product_id not found': product_id})




@app.route('/api/searchblock', methods=['POST'])
def search_block():
    data = request.get_json()
    block_number = data.get('input')
    port = 9545
    # block_number = int(block_number)
    # index = ports_in_use.index(port)
    f=open('blockchain/bcdata.json','r')
    data=json.load(f)
    block_data = data[str(block_number)]
    # w3 = Web3_instances[index]
    # block = w3.eth.get_block(block_number)
    f2=open('blockchain/blockdata.json','w')
    json.dump(block_data,f2)
    # json.dump({'block_number': block.number, 'block_hash': block.hash, 'block_timestamp': block.timestamp},f2)
    return jsonify({'searched for block': block_number})


@app.route('/api/menu', methods=['POST'])
def button_data():
    data = request.get_json()  # Get input data from the request
    a = data.get('input')
    
    if a =='search':
        index = ports_in_use.index(port)
        w3 = Web3_instances[index]
        
    elif a == 'display':
        print("Get blockchain details")
        port = 9545
        index = ports_in_use.index(port)


    # elif a == 'add':
        
    #     print("Add a block")
    #     # port = input("Enter port number of node: ")
    #     port = 9545
    #     # if port in ports_in_use:
    #     index = ports_in_use.index(port)
    #     #     # continue with the rest of the code
    #     # else:
    #     #     print("Port not found in ports_in_use")
    #     w3 = Web3_instances[index]
    #     print('balance before adding block')
    #     print_balance(w3)
    #     # add_block(w3,index)
    #     contract = contracts[index]
    #     f=open('blockchain\\formdata.json','r')
    #     data=json.load(f)
    #     descr = data['descr']
    #     p=data['prevAddr']
    #     if p=="":
    #         prev_addr = []
    #     else:
    #         prev_addr = list(map(int,p.split(" ")))
    #     product_id=data['productId']
    #     balance_before = w3.eth.get_balance(w3.eth.accounts[0])
    #     trans = contract.functions.addBlock(descr,prev_addr,product_id).transact({'from':w3.eth.accounts[0]})
    #     receipt = w3.eth.wait_for_transaction_receipt(trans)
    #     gas_cost = receipt['gasUsed']
    #     print("Gas used:", gas_cost)
    #     print("Transaction receipt:", receipt)

    #     receipt_data = {
    #         'balance-before': balance_before,
    #         'transaction_hash': receipt['transactionHash'].hex(),
    #         'gas_used': receipt['gasUsed'],
    #         'status': receipt['status'],
    #         'from': receipt['from'],
    #         'to': receipt['to'],
            
    #         # 'time_stamp' : datetime.fromtimestamp(receipt['timestamp']),
    #         'balance-after': w3.eth.get_balance(w3.eth.accounts[0])
    #     }
    #     print('receipt data', receipt_data)
    #     with open('blockchain/receipt.json', 'w') as f:
    #         json.dump(receipt_data, f)
    #     print('written to recept file')



    #     print('balance after adding block')
    #     print_balance(w3)

   

    else:
        print("Invalid choice")


    with open('blockchain/buttondata.json','w') as f:
        json.dump({'buttonname': button_data}, f)

    return jsonify({'processed': button_data})


@app.route('/api/process', methods=['POST'])
def process_data():
    data = request.get_json()  # Get input data from the request
    descr = data.get('descr')
    prevAddr = data.get('prevAddr')
    productId = data.get('productId')
    with open('blockchain/formdata.json','w') as f:
        json.dump({'descr': descr, 'prevAddr': prevAddr, 'productId': productId}, f)
    add_block(Web3_instances[0],0)
    return jsonify({'processed': data})


@app.route('/api/blockdetails', methods=['GET'])
def get_block_details():
    with open('blockchain/blockdata.json') as file:
        json_data = json.load(file)
    return jsonify(json_data)

@app.route('/api/data', methods=['GET'])
def get_data():
    port = 9545
    index = ports_in_use.index(port)
    print(index)
    w3 = Web3_instances[index]
    contract = contracts[index]
    data={}
    blockchain = contract.functions.getBlockchain().call()
    for i in range(len(blockchain)):
        block = w3.eth.get_block(i)
        n=block["number"]
        data[n] = {'descr': blockchain[i][0], 'prev_blocks': blockchain[i][1], 'product_id': blockchain[i][2], 'block_number': block.number, 'block_hash': block.hash.hex(), 'block_timestamp': datetime.fromtimestamp(block.timestamp).isoformat()}

    print(data)
    with open('blockchain/bcdata.json', 'w') as f:
        json.dump(data, f)
    with open('blockchain/bcdata.json') as file:
        json_data = json.load(file)
    return jsonify(json_data)

@app.route('/api/receipt', methods=['GET'])
def get_receipt():
    with open('blockchain/receipt.json') as file:
        json_data = json.load(file)
    return jsonify(json_data)


@app.route('/api/addrawmaterial', methods=['POST'])
def addrawmaterial():
    # start_node
    data = request.get_json()
    port = 9545
    rawmaterial = data.get('rawmaterial')
    productid = data.get('productid')
    index = ports_in_use.index(port)
    w3 = Web3_instances[index]
    contract = contracts[index]
    trans = contract.functions.addBlock(rawmaterial,[],productid).transact({'from':w3.eth.accounts[0]})
    receipt = w3.eth.wait_for_transaction_receipt(trans)
    gas_cost = receipt['gasUsed']
    print("Gas used:", gas_cost)
    print("Transaction receipt:", receipt)
    balance_before = w3.eth.get_balance(w3.eth.accounts[0])
    receipt_data = {
        'balance-before': balance_before,
        'transaction_hash': receipt['transactionHash'].hex(),
        'gas_used': receipt['gasUsed'],
        'status': receipt['status'],
        'from': receipt['from'],
        'to': receipt['to'],
        
        # 'time_stamp' : datetime.fromtimestamp(receipt['timestamp']),
        'balance-after': w3.eth.get_balance(w3.eth.accounts[0])
    }
    print('receipt data', receipt_data)
    with open('blockchain/receipt.json', 'w') as f:
        json.dump(receipt_data, f)
    data={}
    blockchain = contract.functions.getBlockchain().call()
    for i in range(len(blockchain)):
        block = w3.eth.get_block(i)
        n=block["number"]
        data[n] = {'descr': blockchain[i][0], 'prev_blocks': blockchain[i][1], 'product_id': blockchain[i][2], 'block_number': block.number, 'block_hash': block.hash.hex(), 'block_timestamp': datetime.fromtimestamp(block.timestamp).isoformat()}

    print(data)
    with open('blockchain/bcdata.json', 'w') as f:
        json.dump(data, f)
    
    return jsonify(receipt_data)





if __name__ == '__main__':
    start_node(9545)
    print(Web3_instances)
    # start_node(9090)
    print(Web3_instances)
    app.run(debug=True)
