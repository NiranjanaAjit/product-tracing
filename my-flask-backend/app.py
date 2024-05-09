from flask import Flask, jsonify, request
from flask_cors import CORS
import json
from web3 import Web3, HTTPProvider
from datetime import datetime
import subprocess
import os

# import subprocess
# subprocess.Popen(["ganache-cli -p 9545"])
# subprocess.Popen(["ganache-cli -p 9090"])
# os.system('truffle migrate --network development')
# os.system('truffle migrate --network development9090')


with open('blockchain\\build\\contracts\\gfg.json') as file:
    contract_json = json.load(file)
    contract_abi = contract_json['abi']
    networks = contract_json['networks']
    addresses = [networks[key]['address'] for key in networks.keys()]
    

#global variables
ports_in_use = []
Web3_instances = []
contracts=[]
global_product_id = []
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
    inglobal = True
    prev_addr = []
    if p=="":
        prev_addr = []
    else:
        prev_addr = list(map(str,p.split(" ")))
    
        for i in prev_addr:
            if i not in global_product_id:
                receipt_data = {'message': 'product ID '+i+' not found '}
                inglobal = False
                break
            if inglobal == False:
                break
        

    if inglobal :
        product_id=data['productId']
        if product_id in global_product_id:
            receipt_data = {'message': 'product ID '+product_id+' already exists'}
        else:
            print('list of prev_addr', prev_addr)
            global_product_id.append(product_id)
            print('global product id ',global_product_id)
            balance_before = w3.eth.get_balance(w3.eth.accounts[0])
            if prev_addr==[]:
                trans = contract.functions.addBlock(descr,[],product_id).transact({'from':w3.eth.accounts[0]})
            else:
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
    deployed_contract_address = ''
    if port == 9545:
        deployed_contract_address = '0xB6B3623C5433Dfe6C5cEcc3CCdCFC832CA017Afc'
        print('contract address of 9545 ', deployed_contract_address)
        # load contract info as JSON
        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  
            
            # fetch contract's abi - necessary to call its functions
            contract_abi = contract_json['abi']
            # print(contract_abi)
        contract = w3.eth.contract(address = deployed_contract_address, abi = contract_abi)
        # print(contract)
        contracts.append(contract)
        ports_in_use.append(port)
        Web3_instances.append(w3)
    elif port == 9090:
        deployed_contract_address = '0x57210e8298501D5df173726c130f4B93a7F11b0e'
        print('contract address of 9090 ', deployed_contract_address)
        # load contract info as JSON
        with open(compiled_contract_path) as file:
            contract_json = json.load(file)  
            
            # fetch contract's abi - necessary to call its functions
            contract_abi = contract_json['abi']
            # print(contract_abi)
            # print(contract_json)
        contract = w3.eth.contract(address = deployed_contract_address, abi = contract_abi)
        # print(contract)
        contracts.append(contract)
        ports_in_use.append(port)
        Web3_instances.append(w3)

    print(Web3_instances, contracts, ports_in_use)
@app.route('/api/searchchain', methods=['POST'])
def search_chain():
    data = request.get_json()
    port = int(data.get('port'))

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
        if data[n]['prev_blocks']==[]:
            data[n]['prev_blocks']='None'
    print(data)
    with open('blockchain/bcdata.json', 'w') as f:
        json.dump(data, f)
    if len(data)==0:
        with open('blockchain/bcdata.json', 'w') as f:
            json.dump({'message' : {'empty': 'No blocks found'}}, f)
    return jsonify({'searched for chain': port})



@app.route('/api/searchblock',methods = ['POST'])
def search_with_product_id():
    data = request.get_json()
    product_id = data.get('input')
    # port = data.get('port')
    # port = int(port)
    found = False
    for  port in ports_in_use:
        index = ports_in_use.index(port)
        w3 = Web3_instances[index]
        contract = contracts[index]
        blockchain = contract.functions.getBlockchain().call()
        for i in range(len(blockchain)):
            block = w3.eth.get_block(i)
            if blockchain[i][2]==product_id:
                found = True
                block_data = {'port': port, 'descr': blockchain[i][0], 'prev_blocks': blockchain[i][1], 'product_id': blockchain[i][2], 'block_number': block.number, 'block_hash': block.hash.hex(), 'block_timestamp': datetime.fromtimestamp(block.timestamp).isoformat()}
                break
    if found:
        f2=open('blockchain/blockdata.json','w')
        json.dump(block_data,f2)
        return jsonify({'searched for product_id': product_id})
    else:
        block_data = {'message': 'product not found'}
        f2=open('blockchain/blockdata.json','w')
        json.dump(block_data,f2)
        return jsonify({'product_id not found': product_id})



@app.route('/api/hold', methods=['POST'])
def search_block():
    data = request.get_json()
    block_number = data.get('input')
    # for i in ports_in_use:

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
    port =  int(data.get('port'))
    with open('blockchain/formdata.json','w') as f:
        json.dump({'descr': descr, 'prevAddr': prevAddr, 'productId': productId}, f)
    index = ports_in_use.index(port)
    w3 = Web3_instances[index]

    
    add_block(w3,index)
    # add_block(Web3_instances[1],1)
    return jsonify({'processed': data})


@app.route('/api/blockdetails', methods=['GET'])
def get_block_details():
    with open('blockchain/blockdata.json') as file:
        json_data = json.load(file)
    return jsonify(json_data)

@app.route('/api/data', methods=['GET'])
def get_data():
    print('global product id ',global_product_id)
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
    data = request.get_json()  # Get input data from the request
    descr = data.get('descr')
    prevAddr = ""
    productId = data.get('productId')
    port =  int(data.get('port'))
    with open('blockchain/formdata.json','w') as f:
        json.dump({'descr': descr, 'prevAddr': prevAddr, 'productId': productId}, f)
    index = ports_in_use.index(port)
    w3 = Web3_instances[index]
    
    add_block(w3,index)
    # add_block(Web3_instances[1],1)
    return jsonify({'processed': data})


    # start_node
    # Get the path to the project directory

    # data = request.get_json()
    # rawmaterial = data.get('rawmaterial')
    # productid = data.get('productid')
    # port = int(data.get('port'))

    # # start_node(port)
    # print(Web3_instances)
    # index = ports_in_use.index(port)
    # w3 = Web3_instances[index]
    # contract = contracts[index]
    # balance_before = w3.eth.get_balance(w3.eth.accounts[0])
    # if productid in global_product_id:
    #     receipt_data = {'message': 'product ID '+productid+' already exists'}
    #     return jsonify(receipt_data)
    # else: 
    #     trans = contract.functions.addBlock(rawmaterial,[],productid).transact({'from':w3.eth.accounts[0]})
    #     receipt = w3.eth.wait_for_transaction_receipt(trans)
    #     gas_cost = receipt['gasUsed']
    #     print("Gas used:", gas_cost)
    #     print("Transaction receipt:", receipt)
    #     global_product_id.append(productid)
    #     print('global product id ',global_product_id)

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
    #     data={}
    #     blockchain = contract.functions.getBlockchain().call()
    #     for i in range(len(blockchain)):
    #         block = w3.eth.get_block(i)
    #         n=block["number"]
    #         data[n] = {'port': port,'descr': blockchain[i][0], 'prev_blocks': blockchain[i][1], 'product_id': blockchain[i][2], 'block_number': block.number, 'block_hash': block.hash.hex(), 'block_timestamp': datetime.fromtimestamp(block.timestamp).isoformat()}

    #     print(data)
    #     with open('blockchain/bcdata.json', 'w') as f:
    #         json.dump(data, f)
    #     if len(data)==0:
    #         with open('blockchain/bcdata.json', 'w') as f:
    #             json.dump({'message' : {'empty': 'No blocks found'}}, f)    
    #     return jsonify(receipt_data)





if __name__ == '__main__':
    start_node(9545)
    print("started node at 9545")
    start_node(9090)
    print("started node at 9090")
    app.run(debug=True)
