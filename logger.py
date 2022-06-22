from argparse import ArgumentError
import sre_compile
import sys
from colorama import Fore
import os
import random
import string
import shutil
import re

logs = sys.path[0] + \
    '/logs' if os.path.isdir(sys.path[0] + '/logs') else os.getcwd() + '/logs'

if os.path.isfile(logs + '/latest.log'):
    os.remove(logs + '/latest.log')

def __write(message: str):
    """
    Create log file if not exists
    """
    with open(logs + '/latest.log', 'a') as f:
        f.write(message)

def escape(string: str):
    escaped_string = string.replace("\n", "")
    escaped_string = escaped_string.replace("\r", "")
    escaped_string = escaped_string.replace("\t", "")
    escaped_string = re.escape(escaped_string)
    escaped_string = escaped_string.replace("\\", "")
    return escaped_string
    

if __name__ == '__main__':
    raise ImportError('This module can cannot be run as a main module')

def internal_error(type: str):
    if type == "EmptyMessage":
        e("Internal logger error: EmptyMessage: message argument is either None or empty", "logger.py")
        raise Exception("Internal logger error: EmptyMessage: message argument is either None or empty \n")
    elif type == "EmptySource":
        e("Internal logger error: EmptySource: source argument is either None or empty", "logger.py")
        raise Exception("Internal logger error: EmptySource: source argument is either None or empty \n")
    else:
        e("Internal logger error: Unknown", "logger.py")
        raise Exception("Internal logger error: Unknown \n")


def info(message: str = None, source: str = None):
    if message is None or message == "":
        internal_error("EmptyMessage")
    elif source is None or source == "":
        internal_error("EmptySource")
    else:
        escaped_message = escape(message)
        escaped_source = escape(source)
        __write(f"[INFO] {{{escaped_source}}} {escaped_message} \n")
        print(f"{Fore.WHITE} [INFO] {{{source}}} {message} {Fore.RESET}")

def warn(message: str = None, source: str = None):
    if message is None or "":
        internal_error("EmptyMessage")
    elif source is None or "":
        internal_error("EmptySource")
    else:
        escaped_message = escape(message)
        escaped_source = escape(source)
        __write(f"[WARN] {{{escaped_source}}} {escaped_message} \n")
        print(f"{Fore.YELLOW} [WARN] {{{source}}} {message} {Fore.RESET}")

def error(message: str = None, source: str = None):
    if message is None or "":
        internal_error("EmptyMessage")
    elif source is None or "":
        internal_error("EmptySource")
    else:
        escaped_message = escape(message)
        escaped_source = escape(source)
        __write(f"[ERROR] {{{escaped_source}}} {escaped_message} \n")
        print(f"{Fore.RED} [ERROR] {{{source}}} {message} {Fore.RESET}")


    

    

# get full path of log dir

if not os.path.isdir(f"{logs}"):
    os.mkdir(f"{logs}")
#if os.path.isfile(f"{logs}/latest.log"):
#    id = random.choices(string.ascii_uppercase + string.digits, k=11)
#    os.rename(f"{logs}/latest.log", f"{logs}/{''.join(id)}.log.old")

# Aliases for functions

def i(message: str = None, source: str = None):
    info(message, source)
def w(message: str = None, source: str = None):
    warn(message, source)
def e(message: str = None, source: str = None):
    error(message, source)

def inf(message: str = None, source: str = None):
    info(message, source)
def wrn(message: str = None, source: str = None):
    warn(message, source)
def err(message: str = None, source: str = None):
    error(message, source)




def exit():
    id = random.choices(string.ascii_uppercase + string.digits, k=8)
    info("Logger gracefully exiting. ID for this run: " + "".join(id), "logger.py")
    __write("[EXIT] \n")
    if os.path.isfile(logs + '/latest.log'):
        shutil.copy2(f"{logs}/latest.log", f"{logs}/{''.join(id)}.log.old")