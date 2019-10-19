import socket
import re
import yaml

from time import sleep


config = yaml.safe_load(open('config.yml', 'rb'))
HOST = config['HOST']
PORT = config['PORT']
NICK = config['NICK']
PASS = config['PASS']


class Bot(object):
    """"""
    def __init__(self, channel, n_msg_per_sec=100):
        super(Bot, self).__init__()
        self._nickname = NICK
        self.channel = channel
        self.connect(channel)
        # print(NICK, channel, '\n', '-' * (len(NICK + channel) + 1))
        print("{} {}\n{}".format(NICK, channel, '-' * (len(NICK + channel) + 1)))

        self._msg_count = 0
        self.n_msg_per_sec = n_msg_per_sec
