from retry import retry
from client import login
from discogs_client.exceptions import HTTPError

discogs = login().client
screen_desc = "Choose your input database: \n 1 - wantlist \n 2 - collection \n 3 - seller inventory \n"


def choose_database():
    choice = input(screen_desc)
    if choice == '1':
        return wantlist_db()
    elif choice == '2':
        return collection_db()
    elif choice == '3':
        return seller_db()
    else:
        pass


def wantlist_db():
    database = [release.id for release in discogs.identity().wantlist]
    print(" [+] Wantlist database created")
    return database


def collection_db():
    database = [release.id for release in discogs.identity().collection_folders[0].releases]
    print(" [+] Collection database created")
    return database


def seller_db():
    input_user = input("Enter seller name -> ")
    user = discogs.user(input_user)
    print("\n Fetching items...")
    database = [listing.release.id for listing in user.inventory]
    print(" Inventory of " + input_user + " created")
    return database


@retry(HTTPError, delay=5, tries=-1)
def extract_tracklist(rls):
    return discogs.release(rls).tracklist


@retry(HTTPError, delay=5, tries=-1)
def print_release_title_from_discogs(rls):
    print("\n   " + discogs.release(rls).title + "\n***")


@retry(HTTPError, delay=5, tries=-1)
def print_artist_from_discogs(track, rls):
    for artist in discogs.release(rls).artists:
        print(artist.name, end=" ")
    print('- ' + track.title)


def print_track(tracklist, rls):
    for track in tracklist:
        if not track.artists:
            print_artist_from_discogs(track, rls)
        else:
            for artist in track.artists:
                print(artist.name + ' - ' + track.title)


def make_tracklist_from(releases_list):
    print("\n [+] Printing tracklist ...")
    for rls in releases_list:
        tracklist = extract_tracklist(rls)
        # print_release_title_from_discogs(rls)
        print_track(tracklist, rls)
