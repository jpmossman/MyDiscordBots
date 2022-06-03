#!/usr/bin/env python3
import argparse
import requests
import json

class Globals:
    args : argparse.Namespace

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('-b','--bot',default='SpideyBot')
    parser.add_argument('-m','--message')
    Globals.args = parser.parse_args()
    return Globals.args

def main():
    # Parse arguments
    parse_args()
    
    # Load pre-written messages and configuration file
    messages_dict = json.load(open('discord-messages.json'))
    config_dict = json.load(open('discord-message.conf'))

    # Get message
    url = config_dict['webhooks'][Globals.args.bot]['url']

    # Send message
    requests.post(url=url, json={'content':Globals.args.message})

if __name__ == '__main__':
    main()
