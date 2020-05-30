from __future__ import unicode_literals
import youtube_dl as you

output = {}
with you.YoutubeDL(output)as out:
    out.download(["https://www.youtube.com/watch?v=lVLDyZCZfh8"])