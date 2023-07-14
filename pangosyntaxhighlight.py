#!/usr/bin/env python3
# vim:expandtab:shiftwidth=2:tabstop=2:smarttab:
# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain 
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.


import pangopygments
import argparse
from pygments.lexers import get_all_lexers


class ListAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if option_string == '--list-languages':
            vals = [];
            for l in get_all_lexers():
                l = l[1]
                if len(l) >= 1:
                    vals.append(l[0])
            print('Available languages: ' + ', '.join(vals))
            pass
        else:
            print('uh oh')
        parser.exit()


parser = argparse.ArgumentParser(description='Syntax highlight code in Pango format using Pygments')
parser.register('action', 'list', ListAction)
parser.add_argument('inputfile', type=argparse.FileType('r'), help='the input file')
parser.add_argument('outputfile', type=argparse.FileType('w'), help='the output file')
parser.add_argument('--language', help='the syntax language of the input file (otherwise auto-detected)', default='auto')
parser.add_argument('--list-languages', help='list available languages (lexers)', nargs=0, action='list')
args = parser.parse_args()

input_data = args.inputfile.read()

output_data = pangopygments.highlight(input_data, args.language)

args.outputfile.write(output_data)

