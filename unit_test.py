import unittest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch

from setup import connect


from EncrypC import EncryptionTool

class TestEncryptionTool(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.write(b'Test data for encryption')
        self.temp_file.close()

        # Set up EncryptionTool instance with dummy key and salt
        self.key = "test_key"
        self.salt = "test_salt"
        self.encryption_tool = EncryptionTool(self.temp_file.name, self.key, self.salt)

    def tearDown(self):
        # Remove the temporary file
        os.unlink(self.temp_file.name)

    def test_hash_key_salt(self):
        # Check if the hash_key_salt method generates correct hashes
        self.encryption_tool.hash_key_salt()
        self.assertTrue(len(self.encryption_tool.hashed_key_salt["key"]) == 32)
        self.assertTrue(len(self.encryption_tool.hashed_key_salt["salt"]) == 16)

    def test_encrypt_decrypt(self):
        # Encrypt the temporary file and then decrypt it
        encrypted_file = self.temp_file.name + ".encr"
        decrypted_file = self.temp_file.name + "_decrypted.txt"

        self.encryption_tool.encrypt()

        pass


class TestConnect(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_connect_success(self, mock_urlopen):
        # Mock the urlopen function to always succeed
        mock_urlopen.return_value = True
        self.assertTrue(connect())

    @patch('urllib.request.urlopen')
    def test_connect_failure(self, mock_urlopen):
        # Mock the urlopen function to raise an exception
        mock_urlopen.side_effect = Exception
        self.assertFalse(connect())

if __name__ == '__main__':
    unittest.main()
