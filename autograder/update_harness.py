#!/usr/bin/env python
import urllib

HARNESS_URL = 'https://s3-us-west-2.amazonaws.com/gradescope-static-assets/autograder/harness.py'


def version(harness_string):
    """ Returns the version from the second line, which looks like
    # Version: 0.10.0
    """
    lines = harness_string.split("\n")
    version_string = lines[1][11:]
    return [int(x) for x in version_string.split(".")]


def is_newer_version(new, old):
    for digit in range(0, 3):
        if new[digit] > old[digit]:
            return True
    return False


def update_harness():
    new_harness = urllib.urlopen(HARNESS_URL).read()
    with open("/autograder/harness.py", "r") as f:
        old_harness = f.read()

    new_version = version(new_harness)
    old_version = version(old_harness)

    if is_newer_version(new_version, old_version):
        with open("/autograder/harness.py", "w") as f:
            f.write(new_harness)

if __name__ == "__main__":
    update_harness()
