#!/bin/env python
import argparse
from os import listdir

from fasternix_stratalorn import get as translators
from fasternix_stratalorn.helpers import (convert_JSON_to_dict, format_list, read_file,
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

def remove_author_username(list_of_contributors):
    """Remove the username of the author from the list of contributors

    :param list_of_contributors: A list, the list of contributors
    """

    authors_username = 'EragonJ'
    authors_username_transifex = 'eragonj'

    if authors_username in list_of_contributors:
        list_of_contributors.remove(authors_username)

    if authors_username_transifex in list_of_contributors:
        list_of_contributors.remove(authors_username_transifex)

    return list_of_contributors


def thanks(username, output=''):
    """Get contributors, translators and append index which are under add_it

    :param username: A string, the Transifex username of a maintainer of the project
    :param output:  A string, the destination of the thanks.json
    """

    thanks = {}
    thanks['contributors'] = contributors('EragonJ/Kaku', return_list=True)
    thanks['translators'] = translators(
        username, 'desktop-app', return_list=True)

    to_add = get_list_file_to_add()
    indexes = to_add['index']
    list_of_files = to_add['files']

    if output != '' and not output.endswith('/'):
        output += '/'

    for i in range(len(list_of_files)):
        data = convert_JSON_to_dict(
            read_file(list_of_files[i]))[indexes[i]]

        if indexes[i] == 'contributors' or indexes[i] == 'translators':
            for element in data:
                if element not in thanks[indexes[i]]:
                    thanks[indexes[i]].extend([element])
                    
            thanks[indexes[i]] = format_list(remove_author_username(thanks[indexes[i]]))

            save_dict_to_JSON({indexes[i]:thanks[indexes[i]]}, list_of_files[i])
        else:
            thanks[indexes[i]] = data

    save_dict_to_JSON(thanks, output + 'thanks.json')
    return


parser = argparse.ArgumentParser(
    description="Generate the famous \033[1m\033[96mthanks.json\033[0m of \033[1m\033[33mKaku\033[0m. \
    More informations about Kaku at \033[1m\033[33mhttps://github.com/EragonJ/Kaku\033[0m",
    epilog="Crafted with \033[1m\033[31m♥\033[0m by \033[1mNissar Chababy (Funilrys)\033[0m")

parser.add_argument("username", type=str,
                    help="Transifex username. \033[1m\033[31mMust be a maintainer of Kaku's Transifex project\033[0m")
parser.add_argument("-o", "--output", type=str,
                    help="Define where \033[1m\033[96mthanks.json\033[0m is gonna be saved")

args = parser.parse_args()
transifex_username = args.username

if args.output:
    thanks(transifex_username, args.output)
else:
    thanks(transifex_username)
