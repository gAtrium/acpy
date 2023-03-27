from argparse import ArgumentParser
from time import sleep
from src.netreq import setContractAddress, requestPrice, requestSymbol
from src.grapher import setGraphSymbol, startGraphThread,addPrice, initanim
from src.contracts import contract_list
import threading

def priceThread():
    while True:
        price = requestPrice()
        if price is not None:
            addPrice(price)
        else:
            print("An error occured while trying to get the price for token")
        sleep(4) # As observed from Trader Joe's request intervals
    
if __name__ == "__main__":
    parser = ArgumentParser(
        prog="acpy", 
        description="A python script that utilizes graphql traderjoe subgraph to pull prices from Avalanche's C-Chain tokens")
    parser.add_argument("-c", "--contract", help="Address of the contract present on the C-Chain")
    parser.add_argument("--token", "-t", choices=contract_list.keys(), required=False, default="PNG", help="Use a built in contract address if you prefer")

    args = parser.parse_args()
    if args.contract is None and args.token is None:
        parser.print_help()
        exit(0)
    contract_addr = ""
    if args.token is not None:
        contract_addr = contract_list[args.token]
    else:
        contract_addr = args.contract
    symbol = setContractAddress(contract_addr)
    
    if symbol is None:
        print("Error while getting the contract symbol.")
        exit(1)
    
    setGraphSymbol(symbol)
    initanim()
    pricethread = threading.Thread(target=priceThread)
    pricethread.start()
    startGraphThread()
