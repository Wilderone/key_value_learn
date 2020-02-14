import json
import os
import tempfile
import argparse
from json import JSONDecodeError


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
f = open(storage_path, 'a+')
f.close()

parser = argparse.ArgumentParser()
parser.add_argument('-k', '--key', help='key')
parser.add_argument('-v', '--val', help='value')
parser.add_argument('-vw', '--view', action='store_true')
args = parser.parse_args()


def write_to_file(key, val):
    with open(storage_path, 'r+') as file_r:
        loaded_data = file_r.read()
    if len(loaded_data) == 0:
        dic = dict(loaded_data)
        dic[key] = val
        with open(storage_path, 'w') as file_wr:
            json.dump(dic, file_wr)
    else:
        json_data = json.loads(loaded_data)
        if key in json_data:
            c = json_data[key] + ", " + val
            json_data.update({key: c})
        else:
            json_data[key] = val
        with open(storage_path, 'w') as file_wr:
            json.dump(json_data, file_wr)


def find_value(key):
    try:
        with open(storage_path, 'r+') as read_file:
            read_file.seek(0)
            json_unpack = json.load(read_file)
            if key in json_unpack:
                print(json_unpack[key])
            elif key not in read_file:
                print("")
    except JSONDecodeError:
        print("")


if args.view:
    with open(storage_path, 'r') as read_file:
        print(read_file.read())


if args.key and args.val:
    write_to_file(args.key, args.val)

if args.key and args.val is None:
    find_value(args.key)
