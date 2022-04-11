"""
Usage:
    rest_helper.py [-n NUMBER] [-c CONFIG_FILE]
    rest_helper.py [--num NUMBER] [--config CONFIG_FILE]
    rest_helper.py -h | --help

Options:
    -h --help                   Show usage and arguments of script
    -n --num NUMBER             Number of lines printed
    -c --config CONFIG_FILE     Path to config file
"""

import re
import sys
from docopt import docopt
import readcfg

def get_section_values(cfg):
    """
    :param cfg: Constructor
    :return: Return dict that contain Section: values
    """
    section = cfg.read_section()
    section_by = {}
    for section_name in section:
        section_values = cfg.read_values(section_name)
        section_by[section_name] = section_values
    return section_by

def return_output(cfg, url_section, data_section, row):
    """
    :param cfg: Constructor
    :param url_section: URL Section with section name and values
    :param data_section: DATA Section with section name and values
    :param row: Number of rows to be printed
    :return: Concatenated link
    """
    links = []
    username = data_section['Data']['username']
    urlpath = data_section['Data']['urlpath']
    for values in url_section.values():
        urls = [urls for urls in values.values()]
        if(len(urls)<row):
            return sys.exit("Not so many values. Please provide a lower number!")
        for index, url in enumerate(urls):
            if(index>row-1):
                break
            protocol = list(filter(bool, re.split(r"^(.*?\//)", url)))[0]
            domain = list(filter(bool, re.split(r"^(.*?\//)", url)))[1]
            links.append(cfg.concat_values(protocol, username, '@', domain, urlpath))
    return links


def main():
    args = docopt(__doc__)
    if args['--config'] and args['--num']:
        cfg = readcfg.ReadCfg(args['--config'])
        for key, value in get_section_values(cfg).items():
            if key == 'Data':
                data_section = {key: value}
            elif key == 'Urls':
                url_section = {key:value}
        for link in return_output(cfg, url_section, data_section, int(args['--num'])):
            print(link)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()