import requests
import time

# A radio livestream
stream_url = "https://icecast.omroep.nl/radio1-bb-mp3"

r = requests.get(stream_url, stream=True)

# Open it and after 10 seconds close the connection
with open('stream.mp3', 'wb') as f:
    # Get the stopping time as a UNIX timestamp
    stop_after = time.time() + 0.5

    try:
        for block in r.iter_content(1024):
            f.write(block)
            if time.time() > stop_after:
                break
    except KeyboardInterrupt:
        pass