import os
import re
import logging
from subprocess import PIPE, Popen

class DBTRunner():
    # 
    #  Initialisation code goes here
    # 
    def exec_dbt(self, workingdir, args=None):
        if args is None:
            args = ["run"]

        final_args = ['dbt']
        final_args.append('--single-threaded')
        final_args.extend(args)
        final_args.extend(['--profiles-dir', "../."])

        proc = Popen(final_args, stdout=PIPE, cwd=workingdir)
        output = proc.communicate()
        
        return output
        
        