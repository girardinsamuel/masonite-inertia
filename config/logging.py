""" Logging Settings """

import os

from masonite import env

"""Default Channel
The default channel will be used by Masonite whenever it needs
to use the logging channel. You can switch the channel at
any time.
"""

DEFAULT = env('LOG_CHANNEL', 'single')

"""Channels
Channels dictate how logging drivers will be initialized.

Supported Channels: single, daily, stack, terminal, slack, syslog
"""

CHANNELS = {
    'timezone': env('LOG_TIMEZONE', 'UTC'),
    'single': {
        'driver': 'single',
        'level': 'debug',
        'path': 'storage/logs/single.log'
    },
    'stack': {
        'driver': 'stack',
        'channels': ['single', 'daily', 'slack', 'terminal']
    },
    'daily': {
        'driver': 'daily',
        'level': 'debug',
        'path': 'storage/logs'
    },
    'terminal': {
        'driver': 'terminal',
        'level': 'info',
    },
    'slack': {
        'driver': 'slack',
        'channel': '#bot',
        'emoji': ':warning:',
        'username': 'Logging Bot',
        'token': env('SLACK_TOKEN', None),
        'level': 'debug'
    },
    'syslog': {
        'driver': 'syslog',
        'path': '/var/run/syslog',
        'level': 'debug'
    }
}
