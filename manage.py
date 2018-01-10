from manager import Manager
from quadcore.tests.manual import ManualTest

import quadcore.tests
import unittest

manager = Manager()

manual_test_pair = {
    "rss": ManualTest.rss,
    "github": ManualTest.github,
    "data": ManualTest.data
}

@manager.command
def run_manual(category):
    """
    Run the manual test codes for developers.
    """
    if category in manual_test_pair:
        manual_test_pair[category]()
    else:
        print("[-] No methods available.")

if __name__ == '__main__':
    manager.main()