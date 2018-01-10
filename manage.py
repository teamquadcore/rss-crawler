from manager import Manager
from quadcore.tests.manual import ManualTest

import quadcore.tests
import unittest

manager = Manager()

@manager.command
def run_manual(category):
    """
    Run the manual test codes for developers.
    """
    if category == "rss":
        ManualTest.rss()
    elif category == "github":
        ManualTest.github()
    elif category == "linkedin":
        print("[-] Not supported yet!")
    elif category == "data":
        ManualTest.data()
    else:
        print("[-] No methods available.")

if __name__ == '__main__':
    manager.main()