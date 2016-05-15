#!/usr/bin/python
#vim: set fileencoding=utf8

from taskfile import *

tf = taskfile("/home/quentin/tasks")

tf.add("foo")

print(tf)

tf.save()
