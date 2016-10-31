#!/usr/bin/env python3

"""

A python 3 fstab parser/editor library.

"""

import tempfile # To create a file in memory

class Fstab():
    """ Creates or opens a new fstab file. """

    def __init__(self,path):
        """ Initiates the fstab file object for parsing """
        print('Initiated object, passed:' + path)

        self.fstab_file = path

        if (self.fstab_file == False) or (self.fstab_file == None) :
            self.create(self.fstab_file)
        else:
            self.read(self.fstab_file)

    def create(self):
        """ Create a new fstab file, hold it in memory until it is written to disk """

    def read(self, path):
        """ Loads /etc/fstab unless an alternate file path is passed"""
        print('Passed' + path)
        with open('path', 'r') as f:
             fstab = f.read()
            return fstab

    def write(self):
        """ Writes the file back to the disk"""
        print('Wrote fstab file')

    def add_entry(self):
        """Adds a fstab entry"""
        print('Adds fstab entry')

    def remove_entry(self):
        """
        Removes a fstab entry.

        Supported modes of operation:
        UUID
        Label
        Device file path
        Mount point
        """
        print('Removes fstab entry ')

    def error_check(self):
        """ Parses fstab file for syntax errors """
        print('Checking fstab for errors')

if __name__ == '__main__':
    print('pyfstab is not callable directly.')
