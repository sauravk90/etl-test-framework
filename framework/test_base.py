import unittest
from sys import platform
from framework.utils import load_env_configs

class TestBase(unittest.TestCase):

    def setUp(self):
        """ Setup method for tests """

        # load .env configurations
        load_env_configs()
        if platform == "win32":
            # for windows
            pass

        elif platform in ["linux", "linux2"]:
            # for linux
            pass

        elif platform in ["darwin", "os2", "os2emx"]:
            # for Mac
            pass

        else:
            # unsupported platform
            raise RuntimeError("Unable to complete test setup, running on an unsupported platform.")

        print("**** test {} setup completed. ****".format(self._testMethodName))


    def tearDown(self):
        """ Tear down method for tests """
        print("**** test {} run finished. ****".format(self._testMethodName))
