from tracklist import choose_database, make_tracklist_from

while True:
    try:
        releases = choose_database()
        print(releases)
        make_tracklist_from(releases)
    # except NameError:
    #     print(" [-] Wrong name, try again")
    #     pass
    except TypeError:
        print(" [-] Wrong input")
        pass
    except KeyboardInterrupt:
        print(" [+] closing program ")
        exit()
