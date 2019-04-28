import unittest
import subprocess
from find import find


class TestFind(unittest.TestCase):

    callback_data = list()

    def store_callback(self, path):
        self.callback_data.append(path)

    def test_standard(self):
        self.callback_data = list()
        find(paths='/tmp', **{'callback': self.store_callback})
        with subprocess.Popen('find /tmp', stdout=subprocess.PIPE, shell=True) as process:
            for i, line in enumerate(process.stdout.readlines()):
                decode_line = line.decode('utf-8').rstrip()
                if decode_line.startswith('find:'):
                    continue
                self.assertEqual(decode_line, self.callback_data[i])
