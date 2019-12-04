#! usr/bin/env python3
# -*- coding: utf-8 -*-

from tracklist import choose_database, print_from_url, make_tracklist_from
import sys

try:
    try:
        releases = choose_database()[0]
    except IndexError:
        releases = print_from_url()
    # write()
    make_tracklist_from(releases)
    sys.stdout.close()
    exit()
except KeyboardInterrupt:
    print (" [+] closing program ")
    sys.stdout.close()
    exit()