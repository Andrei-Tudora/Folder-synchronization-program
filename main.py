import hashlib
import os
import time
import shutil
import argparse
import logging

source = "source"
replica = "replica"
log_file = "log.txt"

if not os.path.exists(source):
    os.makedirs(source)
if not os.path.exists(replica):
    os.makedirs(replica)
if not os.path.exists(log_file):
    with open(log_file, 'w'):
        pass
parser = argparse.ArgumentParser(description='Synchronization program')
parser.add_argument('--source', type=str, default="source", help='Source folder path')
parser.add_argument('--replica', type=str, default="replica", help='Replica folder path')
parser.add_argument('--log-file', type=str, default='log.txt', help='Log file path')
parser.add_argument('--time-interval', type=int, default=10, help='Time interval in seconds')
args = parser.parse_args()

logging.basicConfig(filename=args.log_file, level=logging.INFO, format='%(asctime)s [%(levelname)s]: %(message)s')

def compare_files(file1, file2):
    with open(file1, "rb") as file1, open(file2, "rb") as file2:
        return hashlib.md5(file1.read()).hexdigest() == hashlib.md5(file2.read()).hexdigest()

try:
    while True:
        if not os.path.exists(args.source):
            print("Source directory does not exist. Please create one.")
            while not os.path.exists(args.source):
                time.sleep(1)
            print("Source directory was created")
        if not os.path.exists(args.log_file):
            with open(log_file, 'w'):
                pass
        if not os.path.exists(args.replica):
            os.makedirs(args.replica)
        files_source = os.listdir(args.source)
        files_replica = os.listdir(args.replica)

        for file in files_source:
            source_file_path = os.path.join(args.source, file)
            replica_file_path = os.path.join(args.replica, file)

            if file in files_replica:
                if not compare_files(source_file_path, replica_file_path):
                    os.remove(replica_file_path)
                    shutil.copy2(source_file_path, replica_file_path)
                    logging.info(f"{file} has been copied.")
                    print(f"{file} has been copied.")
            else:
                shutil.copy2(source_file_path, replica_file_path)
                logging.info(f"{file} has been created.")
                print(f"{file} has been created.")

        for file in files_replica:
            if file not in files_source:
                os.remove(os.path.join(args.replica, file))
                logging.info(f"{file} has been deleted.")
                print(f"{file} has been deleted.")
        time.sleep(args.time_interval)
except KeyboardInterrupt:
    print("The loop was stopped with Ctrl+C.")
    raise SystemExit


