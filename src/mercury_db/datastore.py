import time
import json
from threading import *
import concurrent.futures
import getpass
import os
import platform

MAX_DATA_SIZE = 1000000000
MAX_VAL_SIZE = 16384


class DataStore:
    current_platform = platform.system()

    commands_history = []

    cur_dir_path = os.getcwd()

    if current_platform == 'Windows':
        home_path = 'C:/Users/' + getpass.getuser()
        datastore_file_path = 'C:/Users/' + getpass.getuser() + '/datastore.json'
    else:
        home_path = '/home/' + getpass.getuser()
        datastore_file_path = '/home/' + getpass.getuser() + '/datastore.json'

    def __init__(self):
        self.datastore = {}

    def create(self, key, value, time_to_live=0):
        """
        Create operation
        Use syntax : datastore_obj.create(key, value, time_to_live) where time_to_live is optional and is in seconds
        """
        t1 = Thread(target=(self.__create_utility), args=(
            key, value, time_to_live))
        t1.daemon = True
        t1.start()

    # Utility method for performing create operation

    def __create_utility(self, key, value, time_to_live=0):
        if key in self.datastore:
            print('error: This key already exists.')
        else:
            if len(self.datastore) < MAX_DATA_SIZE and len(value) < MAX_VAL_SIZE:
                if time_to_live == 0:
                    data = {'value': value, 'time_to_live': time_to_live}
                else:
                    data = {'value': value,
                            'time_to_live':  time.time() + time_to_live}
                if len(key) <= 32:
                    self.datastore[key] = data
                    # output to file
                    with open(self.datastore_file_path, "w") as outfile:
                        outfile.write(json.dumps(self.datastore))
                else:
                    print('The keys must be 32 characters in length')
            else:
                print('error: Memory limit exceeded')

    def read(self, key):
        """
        Read operation
        Use syntax : datastore_obj.read(key)
        """
        with concurrent.futures.ThreadPoolExecutor(3) as executor:
            future = executor.submit(self.__read_utility, key)
            return future.result()

    # Utility method for performing read operation
    def __read_utility(self, key):
        try:
            with open(self.datastore_file_path, "r") as openfile:
                self.datastore = json.loads(openfile.read())
        except Exception as e:
            print('File not Found.', e)
        if key not in self.datastore:
            print('error: Given key does not exist in datastore')
            return
        else:
            data = self.datastore[key]
            if data['time_to_live'] != 0:
                if time.time() < data['time_to_live']:
                    return json.dumps({key: self.datastore[key]['value']})
                else:
                    print('error: Time of key ' + key + ' has expired')
                    return
            else:
                # data = self.datastore[key]
                return json.dumps({key: self.datastore[key]['value']})

    def delete(self, key):
        """
        Delete operation
        Use syntax : datastore_obj.delete(key)
        """
        t3 = Thread(target=(self.__delete_utility),
                    args=(key,))
        t3.daemon = True
        t3.start()

    # Utility method for performing delete operation
    def __delete_utility(self, key):
        try:
            with open(self.datastore_file_path, "r") as openfile:
                self.datastore = json.loads(openfile.read())
        except Exception:
            print('File not Found.')
        if key not in self.datastore:
            print('error: Given key does not exist in datastore')
        else:
            data = self.datastore[key]
            if data['time_to_live'] != 0:
                if time.time() < data['time_to_live']:
                    del self.datastore[key]
                    with open(self.datastore_file_path, "w") as outfile:
                        outfile.write(json.dumps(self.datastore))
                    print('Success : The record with key ' +
                          key + ' is successfully deleted.')
                else:
                    print('error: Time of key ' + key + ' has expired')
            else:
                del self.datastore[key]
                with open(self.datastore_file_path, "w") as outfile:
                    outfile.write(json.dumps(self.datastore))
                print('Success : The record with key ' +
                      key + ' is successfully deleted.')

    def update(self, key, value):
        """
        Update / Modify operation within its expiry time
        Use syntax : datastore_obj.update(key, value)
        """
        t4 = Thread(target=(self.__update_utility), args=(
            key, value))
        t4.daemon = True
        t4.start()

    def __update_utility(self, key, value):
        try:
            with open(self.datastore_file_path, "r") as openfile:
                self.datastore = json.loads(openfile.read())
        except Exception:
            print('File not Found.')
        if key not in self.datastore:
            print('error: Given key does not exist in datastore')
        else:
            data = self.datastore[key]
            if data['time_to_live'] != 0:
                if time.time() < data['time_to_live']:
                    self.datastore[key]['value'] = value
                    print('Success : The record with key ' +
                          key + ' is successfully updated.')
                    with open(self.datastore_file_path, "w") as outfile:
                        outfile.write(json.dumps(self.datastore))
                    # After updation, read() is called to display the updated value
                    self.read(key)
                else:
                    print('error: Time of key ' + key +
                          ' has expired.')
            else:
                self.datastore[key]['value'] = value
                print('Success : The record with key ' +
                      key + ' is successfully updated.')
                with open(self.datastore_file_path, "w") as outfile:
                    outfile.write(json.dumps(self.datastore))
                # After updation, read() is called to display the updated value
                self.read(key)
