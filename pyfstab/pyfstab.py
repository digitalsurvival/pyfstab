#!/usr/bin/env python3



"""

A python 3 fstab parser/editor library.

Fstab class expects a valid path to be passed or /etc/fstab to exist. If not it will create a file object that will
need written to the disk.

"""

import tempfile # To create a tmp file if /etc/fstab doesn't exist and no file is passed.
import os.path

class Fstab():
    """ Creates or opens a new fstab object. """

    def __init__(self,path='/etc/fstab'):
        """ Initiates the fstab file object for parsing """
        self.fstab_file = path

        if (str(self.fstab_file) == True) and (os.path.isfile(self.fstab_file) == True):
            # We have a (valid) file!
            self.read(self.fstab_file)
        else:
            self.create(self, path=None, header=True)

    #todo
    def create(self, header=True, description=False):
        """ Create a new fstab file.

            Optional arguments:

            header (True/False) - Appends a long header to the top of the file.
            description (True/False) - Appends a small definition to the top of the file (use this if header = False
            path - Will create a file on the disk immediately at this location. Defaults to tempfile in memory

            """
        t = tempfile.NamedTemporaryFile

        #todo
        if header == True:
            pass
        #todo
        if description == True:
            # <fs>			<mountpoint>	<type>		<opts>		<dump/pass>
            pass
    #todo
    def read(self, path):
        """ Loads /etc/fstab unless an alternate file path is passed"""
        print('Passed' + path)
        with open('path', 'r') as f:
             fstab = f.read()
            return fstab
    #todo
    def write(self):
        """ Writes the file back to the disk"""
        print('Wrote fstab file')
    #todo
    def add_entry(self):
        """Adds a fstab entry"""
        print('Adds fstab entry')
    #todo
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

    #todo
    def parse(self):
        """ Parses fstab file for syntax errors """
        print('Checking fstab for errors')

if __name__ == '__main__':
    print('pyfstab is not callable directly.')
