from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
from datetime import datetime
import random
from dotenv import load_dotenv
import tweepy
import os
import io
import sys
import numpy as np
from PIL import Image, ImageFont, ImageOps, ImageChops
import requests
from random import randint, seed
import json
import math
import PIL

def Random_Alpha():
    l = ['A','B','C','D', 'E', 'F']
    return l[random.randint(0,5)]


def create():

    c_k = os.getenv("API_key")
    c_s = os.getenv("API_secret_key")
    a_k = os.getenv("Access_token")
    a_s = os.getenv("access_token_secret")
    auth = tweepy.OAuthHandler(c_k, c_s)
    auth.set_access_token(a_k, a_s)
    api = tweepy.API(auth)

    quote_font = ImageFont.truetype('test2.ttf', randint(350, 650))
    quote_font1 = ImageFont.truetype('test2.ttf', randint(350, 650))
    quote_font2 = ImageFont.truetype('test2.ttf', randint(350, 650))


    arr2 = [quote_font, quote_font1, quote_font2]

    arr = np.random.randint(0,255,(3000,3000,3))
    im = Image.fromarray(arr,'RGB')

    imgsize=(3000,3000)
    im2 = Image.new('RGB', imgsize, (0, 0, 0))
    im1 = Image.new('RGB', imgsize, (0, 0, 0))



    for i in range(randint(240, 355)):
        draw = ImageDraw.Draw(im1)
        color = (randint(0, 256), randint(0, 256), randint(0, 256))
        draw.multiline_text((randint(-300, 3000),randint(-300, 3000)), Random_Alpha(), color, font=arr2[randint(0, 2)])
        quote_font = ImageFont.truetype('test2.ttf', randint(700, 2000))
        quote_font1 = ImageFont.truetype('test2.ttf', randint(700, 2000))
        quote_font2 = ImageFont.truetype('test2.ttf', randint(700, 2000))
        draw = ImageDraw.Draw(im1)
        arr2 = [quote_font,  quote_font1, quote_font2]


    draw = ImageDraw.Draw(im2)
    for i in range(randint(84, 145)):
        draw = ImageDraw.Draw(im2)
        color = (randint(0, 256), randint(0, 256), randint(0, 256))
        draw.rectangle((randint(0, int(math.ceil(3000 / (i+1)))), randint(0, int(math.ceil(3000 / (i+1)))), randint(0, int(math.ceil(3000 / (i+1)))), randint(0, int(math.ceil(3000 /(i+1))))), fill= color, width=5)
        color = (randint(0, 256), randint(0, 256), randint(0, 256))
        draw.multiline_text((randint(-300, 3000),randint(-300, 3000)), Random_Alpha(), color, font=arr2[randint(0, 2)])
        quote_font = ImageFont.truetype('test2.ttf', randint(1400, 4000))
        quote_font1 = ImageFont.truetype('test2.ttf', randint(1400, 4000))
        quote_font2 = ImageFont.truetype('test2.ttf', randint(1400, 4000))
        draw = ImageDraw.Draw(im1)
        arr2 = [quote_font,  quote_font1, quote_font2]
        im2 = im2.rotate(randint(0, 360))





    im2 = im2.filter(ImageFilter.MaxFilter(size=9))
    im2 = im2.filter(ImageFilter.EDGE_ENHANCE_MORE)
    im2 = im2.filter(ImageFilter.DETAIL)
    im = im.filter(ImageFilter.MaxFilter(size=9))
    im = im.filter(ImageFilter.EDGE_ENHANCE_MORE)

    im2 = ImageChops.difference(im2, im)
    im2 = im2.filter(ImageFilter.MaxFilter(size=9))
    im2 = im2.filter(ImageFilter.EDGE_ENHANCE_MORE)
    im2 = im2.filter(ImageFilter.DETAIL)
    draw = ImageDraw.Draw(im2)

    im2 = im2.filter(ImageFilter.EDGE_ENHANCE_MORE)
    im2 = im2.filter(ImageFilter.DETAIL)
    im2 = im2.filter(ImageFilter.EDGE_ENHANCE_MORE)

    mask = Image.new("L", im1.size, 0)
    draw3 = ImageDraw.Draw(mask)


    draw3 = ImageDraw.Draw(mask)
    draw3.ellipse((1500, 1500, 3000, 3000), fill=255)
    im2 = Image.composite(im2, im1, mask)
    im2 = im2.filter(ImageFilter.MinFilter(size=9))
    im2 = im2.filter(ImageFilter.EDGE_ENHANCE_MORE)
    im2 = im2.filter(ImageFilter.DETAIL)
    for i in range(randint(24, 35)):
        im2 = im2.filter(ImageFilter.EDGE_ENHANCE_MORE)

    im2 = im2.filter(ImageFilter.BLUR)
    im2 = im2.filter(ImageFilter.FIND_EDGES)
    im2 = im2.convert('RGB')


    mapikc= os.getenv('musixmatch')

    albums = ['13710907', '43776035', '11020895']

    trackIds = requests.get(
  'https://api.musixmatch.com/ws/1.1/album.tracks.get?apikey='
  +  mapikc +
  '&album_id=' + albums[randint(0,2)]
)


    ids = trackIds.json()


    lyrics = requests.get(
      'https://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey='
      + mapikc +
      '&track_id=' + str(ids['message']['body']['track_list'][randint(0,len(ids['message']['body']['track_list'])-1 )]["track"]["track_id"])
    )

    lyrics = lyrics.json()


    # print('lyrics_body' in lyrics['message']['body']['lyrics'])

    if('lyrics' in lyrics['message']['body'] and 'lyrics_body' in lyrics['message']['body']['lyrics']):
        i = lyrics['message']['body']['lyrics']['lyrics_body'].upper().split('\n')
        i = list(filter(lambda x : len(x) > 4 , i))
    elif('lyrics_body' in lyrics['message']['body']['lyrics'] == False):
        while('lyrics_body' in lyrics['message']['body']['lyrics'] == False):
                lyrics = requests.get(
                  'https://api.musixmatch.com/ws/1.1/track.lyrics.get?apikey='
                  + mapikc +
                  '&track_id=' + str(ids['message']['body']['track_list'][randint(0,len(ids['message']['body']['track_list'])-1 )]["track"]["track_id"])
                )

                lyrics = lyrics.json()
                i = lyrics['message']['body']['lyrics']['lyrics_body'].upper().split('\n')
                i = list(filter(lambda x : len(x) > 4 , i))


    buf = io.BytesIO()
    im2.save(buf, format='PNG')
    buf.seek(0)
    thing = buf.getvalue()
    test = api.media_upload('art.png',file= buf)
    api.update_status(status=i[randint(0,len(i)-3)], media_ids=[test.media_id])

    # im2.show()
create()
