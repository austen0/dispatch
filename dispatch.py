#!/usr/bin/env python

import argparse
import config
import requests
from twilio.rest import Client

CLIENT = Client(config.Twilio.ACCOUNT_SID, config.Twilio.AUTH_TOKEN)
JSONBIN_URL = 'https://api.jsonbin.io/b/'


def push(msg, dest):
  if isinstance(msg, list):
    msg = ' '.join(msg)

  # push message to phone
  if dest == 'phone' or dest == 'all':
    CLIENT.api.account.messages.create(
      to=config.Twilio.RECIPIENT,
      from_=config.Twilio.SENDER,
      body=msg
    )

  # push message to json bin
  if dest == 'cloud' or dest == 'all':
    requests.put(
        '{url}{bin_id}'.format(url=JSONBIN_URL, bin_id=config.Jsonbin.BIN_ID),
        json={'message': msg},
        headers={
            'secret-key': config.Jsonbin.API_KEY,
            'content-type': 'application/json'
        }
    )


def pull():
  # print last message from json bin
  r = requests.get(
      '{url}{id}/latest'.format(url=JSONBIN_URL, id=config.Jsonbin.BIN_ID),
      headers={'secret-key': config.Jsonbin.API_KEY}
  )
  print r.json()['message']


def arg_parser():
  # parse runtime flags
  parser = argparse.ArgumentParser(description='dispatch')
  parser.add_argument(
      'message',
      metavar='MESSAGE',
      type=str,
      nargs=argparse.REMAINDER,
      help='Message to be pushed.'
  )
  parser.add_argument(
      '-d',
      type=str,
      choices=['all', 'phone', 'cloud'],
      default='all',
      help='Destination for message (default: all).'
  )
  return parser.parse_args()


def main():
  args = arg_parser()
  if args.message:
    push(args.message, args.d)
  else:
    pull()


if __name__ == '__main__':
  main()
