from __future__ import unicode_literals
import youtube_dl as you

output = {}
with you.YoutubeDL(output)as out:
    # just replace the url with any urlof your choice and you are done
    out.download(["https://www.youtube.com/watch?v=lVLDyZCZfh8"])
