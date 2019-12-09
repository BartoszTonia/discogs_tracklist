#! usr/bin/env python
# -*- coding: utf-8 -*-

from retry import retry
from client import login
from discogs_client.exceptions import HTTPError

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
        input_user = raw_input("Enter seller name -> ")
        user = discogs.user(input_user)
        print "\n Fetching items..."
        database.append([listing.release.id for listing in user.inventory])
        print "Len = " + str(len(database))
        print " Inventory of " + input_user + " created"
    return database[0]


@retry(HTTPError, delay=5, tries=-1)
def extract_tracklist(i):
    return discogs.release(i).tracklist


@retry(HTTPError, delay=5, tries=-1)
def print_artist_from_discogs(track, i):
    for artist in discogs.release(i).artists:
        print artist.name + ' - ' + track.title


def print_track(tracklist, i):
    for track in tracklist:
        if not track.artists:
            print_artist_from_discogs(track, i)
        else:
            for artist in track.artists:
                print artist.name + ' - ' + track.title


@retry(HTTPError, delay=5, tries=-1)
def print_release_title_from_discogs(i):
    print "\n   " + discogs.release(i).title + "\n***"


def make_tracklist_from(releases_list):
    print("\n [+] Printing tracklist ...")
    for i in releases_list:
        tracklist = extract_tracklist(i)
        # print_release_title_from_discogs(i)
        print_track(tracklist, i)
