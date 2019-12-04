#! usr/bin/env python
# -*- coding: utf-8 -*-

from client import login
from time import sleep
import requests as please
import sys, re

discogs = login().client

def choose_database():
    choice = raw_input("Choose your input database: \n 1 - wantlist \n 2 - collection \n 3 - seller inventory \n")
    database = []
    if choice == '1':
        database.append([release.id for release in discogs.identity().wantlist])
        print " [+] Wantlist database created"
    elif choice == '2':
        database.append([release.id for release in discogs.identity().collection_folders[0].releases])
        print " [+] Collection database created"
    elif choice == '3':
        print " [+] Change search engine for url - output max 250 entries sorted by Price"    ## generate IndexError and move to print from url
    return database

def extract_releases_from_url(url):
    response = please.get(url)
    url_list = re.findall('(?:ease/)(\d.*)', response.content)
    id_list = []
    for i in range(len(url_list)):
        id = url_list[i].split('"')
        id_list.append(id[0])
    return id_list

def print_from_url():
    try:
        input = raw_input("Enter seller login: \n ") ## test_names  = ["baton1", "buy24hours", "tedirens"]
        url = "https://www.discogs.com/seller/" + input + "/profile?sort=price%2Cdesc&limit=250&page=1"
                                                                         ## need to add iteration over pages
        releases = extract_releases_from_url(url)
        if not releases:
            raise KeyboardInterrupt
        else:
            return releases
    except KeyboardInterrupt:
        print " [-] Something went wrong \n Default seller - 'baton1'"
        releases = extract_releases_from_url("https://www.discogs.com/seller/BaTon1/profile?sort=price%2Cdesc&limit=250")
        return releases

def make_tracklist_from(releases):
    print(str(releases) + "\n\n [+] Printing tracklist ...")
    for (id) in releases:
        tracklist = discogs.release(id).tracklist
        print "\n   " + discogs.release(id).title + "\n***"
        sleep(0.8)
        for track in tracklist:
            if not track.artists:
                for artist in discogs.release(id).artists:
                    print artist.name + ' - ' + track.title
            else:
                for artist in track.artists:
                    print artist.name + ' - ' + track.title

def write():
    sys.stdout = open("tracklist.txt", "w")