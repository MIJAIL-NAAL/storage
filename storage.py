# Version I

import argparse
import os
import tempfile
import json


def read_storage(storage_path):
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as file:
        raw_data = file.read()
        if raw_data:
            return json.loads(raw_data)
        return {}

def write(storage_data, data):
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))

def parse():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='''
        This program creates a temporary file to store data in a dictionary
        Use these commands: 
            storage.py --key 'KEY' --val 'VALUE' ----> store data
            storage.py --key 'KEY'               ----> print the values of a specific key
            storage.py --all all                 ----> print all data''')
    parser.add_argument("--key", help='Add a key')
    parser.add_argument("--val", help='Add a Value to a specific Key')
    parser.add_argument("--all", help='Print all stored data')
    return parser.parse_args()

def run(storage_path):
    args = parse()

    if args.key and args.val:
        data = read_storage(storage_path)
        data[args.key] = data.get(args.key, list())
        data[args.key].append(args.val)
        write(storage_path, data)

    elif args.key:
        data = read_storage(storage_path)
        print(*(data.get(args.key, [])), sep=', ')

    elif args.all == "all":
        data = read_storage(storage_path)
        print(data)

    else:
        print('The program is called with invalid parameters.')

    

if __name__ == '__main__':
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
    run(storage_path)
    
