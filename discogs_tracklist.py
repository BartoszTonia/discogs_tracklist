#! usr/bin/env python3
# -*- coding: utf-8 -*-

from tracklist import choose_database, make_tracklist_from

try:
    releases = choose_database()[0]
    make_tracklist_from(releases)
    exit()
except KeyboardInterrupt:
    print (" [+] closing program ")
    exit()