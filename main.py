#!/usr/bin/python
#vim: set fileencoding=utf8

import sys, getopt, os

from taskfile import *

def print_usage():
    print("Usage: {} <option> (argument)".format(sys.argv[0]))
    print("Options:")
    print("-h\t\t\tDisplay this help message")
    print("-l\t\t\tList all tasks")
    print("-a <task name>\t\tAdd a task")
    print("-d <task number>\tDelete a task")

def main(args):
    tf = taskfile(os.environ.get("HOME")+"/.config/tasky/.tasks")

    if(len(args) == 0):
        tf.show()
        sys.exit(1)

    try:
        opts, args = getopt.getopt(args, "hla:d:", ["add=", "delete="])
    except getopt.GetoptError:
        print_usage()
        sys.exit(1)

    for opt, arg in opts:
        if opt == "-h":
            print_usage()
        elif opt == "-l":
            tf.show()
        elif opt in ("-a", "--add"):
            tf.add(arg)
        elif opt in ("-d", "--delete"):
            tf.remove(int(arg))

    tf.save()

main(sys.argv[1:])
