#! usr/bin/env python3
# -*- coding: utf-8 -*-

import discogs_client

def login():
    token = raw_input("Paste your token: \n")
    discogs = discogs_client.Client("TracklistDiscogs/0.1", user_token=token)
    me = discogs.identity()
    return me