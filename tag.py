#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from telegram.ext import Updater, CommandHandler
import logging

updater = Updater('727103303:AAGHuYVPUnp-6VX4-PbKc92TlPa8TI36XwY')
logging.basicConfig(filename='mylogs.txt', format='%(asctime)s - %(levelname)s - %(message)s',level=logging.INFO)

def start_method(bot, update):
    bot.sendMessage(update.message.chat_id, "سلام")

def tag_search(bot, update, args):
    args = ' '.join(args)
    with open("osmtags.json", "r") as read_file:
        data = json.load(read_file)
        for tag in data:
            if tag["title"] == args:
                title = tag["title"]
                key = tag["key"]
                value = tag["value"]
                r = '%s\n key= %s\n  value= %s' % (title, key, value)
                bot.sendMessage(update.message.chat_id, r)






start_command = CommandHandler('start', start_method)
tag_search = CommandHandler("tag", tag_search, pass_args=True)
updater.dispatcher.add_handler(start_command)
updater.dispatcher.add_handler(tag_search)

updater.start_polling()


updater.idle()
