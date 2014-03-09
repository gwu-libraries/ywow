#!/usr/bin/env python

import argparse
import os
import traceback

import dropbox

import config


def walk(path, client, args):
    if args.verbose:
        print 'path:', path
    for loc in os.walk(path):
        curpath, dirs, files = loc
        for f in files:
            fullname = os.path.abspath(os.path.join(curpath, f))
            if args.verbose:
                print 'file: %s %s' % (os.stat(fullname).st_size, fullname)
            if args.dryrun:
                continue
            try:
                fp = open(fullname, 'rb')
                response = client.put_file(fullname, fp)
                fp.close()
                if args.verbose:
                    print 'uploaded:', response
            except:
                traceback.print_exc()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Copy a directory to dropbox')
    parser.add_argument('path', help='directory path to copy')
    parser.add_argument('-v', '--verbose', action='store_true',
                        default=False, help='verbose output')
    parser.add_argument('-d', '--dryrun', action='store_true',
                        default=False, help='perform a dry run')
    args = parser.parse_args()
    client = dropbox.client.DropboxClient(config.DROPBOX_ACCESS_TOKEN)
    walk(args.path, client, args)
