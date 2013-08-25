#!/usr/bin/env python

import codecs
import json
import os
import time

from weibo import Client

import config


if __name__ == '__main__':
    c = Client(config.WEIBO_API_KEY, config.WEIBO_API_SECRET,
               config.REDIRECT_URI, token=config.TOKEN)
    timeline = c.get('statuses/public_timeline', count=200)
    gmt = time.gmtime()
    path = '%s/%s' % (config.DATA_DIR, time.strftime('%Y/%m/%d/%H', gmt))
    # create that directory to hold these files if it doesn't yet exist
    try:
        os.stat(path)
    except:
        os.makedirs(path)
    fname_prefix = time.strftime('%Y%m%d-%H%M%SZ', gmt)
    fname_json = '%s/%s.json' % (path, fname_prefix)
    fname_txt = '%s/%s.txt' % (path, fname_prefix)

    # write out the raw data, as utf8-encoded JSON
    fp_json = codecs.open(fname_json, 'wb', encoding='utf-8')
    json.dump(timeline, fp_json, indent=2, ensure_ascii=False,
              encoding='utf-8')
    fp_json.close()
    os.system('gzip %s' % fname_json)

    # write out the same data, but only needed values as delimited text
    fp_txt = codecs.open(fname_txt, 'wb', encoding='utf-8')
    for status in timeline['statuses']:
        row = [status['mid'], status['created_at'],
               status['user']['city'], status['user']['province'],
               status['user']['location'],
               str(status['user']['followers_count']),
               str(status['user']['friends_count']),
               str(status['user']['bi_followers_count']),
               status['user']['gender'],
               str(status['user']['statuses_count']),
               status['text']]
        fp_txt.write(u'\t'.join(row) + '\n')
    fp_txt.close()
    os.system('gzip %s' % fname_txt)
