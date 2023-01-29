#!/usr/bin/env python3

from os import path

# This is an example file that should emphasize that the behavior of the
# code could be dependent on factors outside the file itself. This
# can be a lot of things like environment variables but also other files. In
# this example, the existence of a file `foo.cfg` causes a failure.

if path.exists("foo.cfg"):
    raise ValueError("Failure!")
print("Successful operation")
