from tracklist import choose_database, make_tracklist_from

try:
    releases = choose_database()
    make_tracklist_from(releases)
    exit()
except KeyboardInterrupt:
    print (" [+] closing program ")
    exit()