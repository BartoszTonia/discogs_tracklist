import discogs_client


def login():
    token = input("Paste your token: \n")
    discogs = discogs_client.Client("TracklistDiscogs/0.1", user_token=token)
    return discogs.identity()
