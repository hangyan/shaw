#!/usr/bin/env python
# -*- coding: utf-8 -*-
import fcntl
import logging
import os
import struct
import sys
import time
from logging.handlers import TimedRotatingFileHandler

from colorlog import ColoredFormatter, escape_codes
from colorlog.colorlog import ColoredRecord

__author__ = 'Hang Yan'

LOG = logging.getLogger(__name__)


def fun():
    print "{} %s", "string"


class MultiProcessTimedRotatingFileHandler(TimedRotatingFileHandler):
    def doRollover(self):
        """
        do a rollover; in this case, a date/time stamp is appended to the filename
        when the rollover happens.  However, you want the file to be named for the
        start of the interval, not the current time.  If there is a backup count,
        then we have to get a list of matching filenames, sort them and remove
        the one with the oldest suffix.
        """
        # if self.stream:
        #    self.stream.close()
        # get the time that this sequence started at and make it a TimeTuple
        t = self.rolloverAt - self.interval
        if self.utc:
            timeTuple = time.gmtime(t)
        else:
            timeTuple = time.localtime(t)
        dfn = self.baseFilename + "." + time.strftime(self.suffix, timeTuple)
        # if os.path.exists(dfn):
        #    os.remove(dfn)
        lockdata = struct.pack('hhllhh', fcntl.F_WRLCK, 0, 0, 0, 0, 0)
        fcntl.fcntl(self.stream, fcntl.F_SETLKW, lockdata)
        if not os.path.exists(dfn) and os.path.exists(self.baseFilename):
            os.rename(self.baseFilename, dfn)
            with open(self.baseFilename, 'a'):
                pass
        if self.backupCount > 0:
            # find the oldest log file and delete it
            # s = glob.glob(self.baseFilename + ".20*")
            # if len(s) > self.backupCount:
            #    s.sort()
            #    os.remove(s[0])
            for s in self.getFilesToDelete():
                os.remove(s)
        # print "%s -> %s" % (self.baseFilename, dfn)
        if self.stream:
            self.stream.close()
        self.mode = 'a'
        self.stream = self._open()
        currentTime = int(time.time())
        newRolloverAt = self.computeRollover(currentTime)
        while newRolloverAt <= currentTime:
            newRolloverAt = newRolloverAt + self.interval
        # If DST changes and midnight or weekly rollover, adjust for this.
        if (self.when == 'MIDNIGHT' or self.when.startswith('W')) and not self.utc:
            dstNow = time.localtime(currentTime)[-1]
            dstAtRollover = time.localtime(newRolloverAt)[-1]
            if dstNow != dstAtRollover:
                if not dstNow:  # DST kicks in before next rollover, so we need to deduct an hour
                    newRolloverAt = newRolloverAt - 3600
                else:  # DST bows out before next rollover, so we need to add an hour
                    newRolloverAt = newRolloverAt + 3600
        self.rolloverAt = newRolloverAt


class SplitColoredFormatter(ColoredFormatter):
    def format(self, record):
        """Format a message from a record object."""
        record = ColoredRecord(record)
        record.log_color = self.color(self.log_colors, record.levelname)

        # Set secondary log colors
        if self.secondary_log_colors:
            for name, log_colors in self.secondary_log_colors.items():
                color = self.color(log_colors, record.levelname)
                setattr(record, name + '_log_color', color)

        # Format the message
        if sys.version_info > (2, 7):
            message = super(ColoredFormatter, self).format(record)
        else:
            message = logging.Formatter.format(self, record)

        # Add a reset code to the end of the message
        # (if it wasn't explicitly added in format str)
        if self.reset and not message.endswith(escape_codes['reset']):
            message += escape_codes['reset']

        if '|' in message:
            desc, data = message.split("|", 1)
            desc = desc + escape_codes['reset']
            data = escape_codes['green'] + data
            message = desc + '|' + data

        return message


def _log_request(request, attrs):
    method = request.method
    if method not in ['PUT', 'POST']:
        return
    path = request.get_full_path()
    res = '\n'.join(['{} = {}'.format(x, getattr(request, x, '')) for x in attrs])
    LOG.debug("{} {} | {}".format(method, path, res))


class BodyLoggingMiddleware(object):
    def process_request(self, request):
        _log_request(request, ['body'])


class MetaLoggingMiddleware(object):
    def process_request(self, request):
        _log_request(request, ['META'])


def get_log_config(component, handlers, level='DEBUG', path='/var/log/vfine/'):
    """Return a log config for django project."""
    config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s][%(threadName)s]' +
                          '[%(name)s.%(funcName)s():%(lineno)d] %(message)s'
            },
            'color': {
                '()': 'shaw.log.SplitColoredFormatter',
                'format': "%(asctime)s " +
                          "%(log_color)s%(bold)s[%(levelname)s]%(reset)s" +
                          "[%(threadName)s][%(name)s.%(funcName)s():%(lineno)d] " +
                          "%(blue)s%(message)s"
            }
        },
        'handlers': {
            'debug': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': path + component + '.debug.log',
                'maxBytes': 1024 * 1024 * 1024,
                'backupCount': 5,
                'formatter': 'standard',
            },
            'color': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': path + component + '.color.log',
                'maxBytes': 1024 * 1024 * 1024,
                'backupCount': 5,
                'formatter': 'color',
            },
            'info': {
                'level': 'INFO',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': path + component + '.info.log',
                'maxBytes': 1024 * 1024 * 1024,
                'backupCount': 5,
                'formatter': 'standard',
            },
            'error': {
                'level': 'ERROR',
                'class': 'logging.handlers.RotatingFileHandler',
                'filename': path + component + '.error.log',
                'maxBytes': 1024 * 1024 * 100,
                'backupCount': 5,
                'formatter': 'standard',
            },
            'console': {
                'level': level,
                'class': 'logging.StreamHandler',
                'formatter': 'standard'
            },
        },
        'loggers': {
            'django': {
                'handlers': handlers,
                'level': 'INFO',
                'propagate': False
            },
            'django.request': {
                'handlers': handlers,
                'level': 'INFO',
                'propagate': False,
            },
            '': {
                'handlers': handlers,
                'level': level,
                'propagate': False
            },
        }
    }
    return config
