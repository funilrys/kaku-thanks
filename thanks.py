#!/bin/env python
import argparse
from os import listdir

from fasternix_stratalorn import get as translators
from fasternix_stratalorn.helpers import (convert_JSON_to_dict, read_file,
                                          save_dict_to_JSON)
from obstructing_trio import get as contributors


def get_list_file_to_add():
    """Get the list of file and index to append to thanks.json"""

    DIRECTORY_TO_CHECK = './add_it'

    results = {}
    results['files'] = listdir(DIRECTORY_TO_CHECK)

    list_of_index = []

    for i in range(len(results['files'])):
        content = results['files'][i]
        results['files'][i] = DIRECTORY_TO_CHECK + '/' + content

        list_of_index.extend([content.split('.json')[0]])

    results['index'] = list_of_index

    return results


def thanks(output=''):
    """Get contributors, translators and append index which are under add_it"""

    thanks = {}

    thanks['contributors'] = contributors('EragonJ/Kaku', return_list=True)
    thanks['translators'] = translators(
        'funilrys', 'desktop-app', return_list=True)

    to_add = get_list_file_to_add()
    indexes = to_add['index']
    list_of_files = to_add['files']

    for i in range(len(list_of_files)):
        thanks[indexes[i]] = convert_JSON_to_dict(
            read_file(list_of_files[i]))[indexes[i]]

    save_dict_to_JSON(thanks, output + 'thank.json')
    return


parser = argparse.ArgumentParser()
parser.add_argument(
    "--output", help="define where thanks.json is gonna be located", type=str)
args = parser.parse_args()
if args.output:
    thanks(args.output)
else:
    thanks()
