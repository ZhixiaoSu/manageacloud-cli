import tempfile
import unittest
import ConfigParser
import os

import mock

import maccli.service.auth
import maccli.dao.api_auth
import maccli.helper.http
from mock_data import *


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.user = service.user
        self.apikey = service.apikey

    def tearDown(self):
        service.user = self.user
        service.apiKey = self.apikey

    @mock.patch('dao.api_auth.get_auth')
    def test_auth_authenticate(self, mock_get_auth):
        mock_get_auth.return_value = (MOCK_USER, MOCK_APIKEY)
        maccli.service.auth.authenticate(MOCK_USER, MOCK_PASSWORD)
        self.assertEqual(MOCK_USER, service.user)
        self.assertEqual(MOCK_APIKEY, service.apikey)
        self.tearDown()


    def test_auth_load_from_file(self):
        file = tempfile.NamedTemporaryFile(delete=False)
        with file as f:
            f.writelines(["[auth]\n", "user = %s\n" % MOCK_USER, "apikey = %s\n" % MOCK_APIKEY])
        user_read, apikey_read = dao.api_auth.load_from_file(file.name)
        self.assertEqual(user_read, MOCK_USER)
        self.assertEqual(apikey_read, MOCK_APIKEY)
        os.remove(file.name)

    @mock.patch.object(dao.api_auth.ConfigParser.ConfigParser, 'read', side_effect=ConfigParser.Error)
    def test_auth_load_from_file_with_exception(self, mock_read):
        user_read, apikey_read = dao.api_auth.load_from_file('abc')
        self.assertIsNone(user_read)
        self.assertIsNone(apikey_read)

    def test_auth_is_authenticated(self):
        service.user = MOCK_USER
        service.apikey = MOCK_APIKEY
        self.assertTrue(maccli.service.auth.is_authenticated())

        service.user = None
        service.apikey = MOCK_APIKEY
        self.assertFalse(maccli.service.auth.is_authenticated())

        service.user = MOCK_USER
        service.apikey = None
        self.assertFalse(maccli.service.auth.is_authenticated())

        service.user = None
        service.apikey = None
        self.assertFalse(maccli.service.auth.is_authenticated())


    def test_auth_logout(self):
        service.user = MOCK_USER
        service.apikey = MOCK_APIKEY
        maccli.service.auth.logout()
        self.assertIsNone(service.user)
        self.assertIsNone(service.apikey)


    def test_auth_get_auth_header(self):
        service.user = MOCK_USER
        service.apikey = MOCK_APIKEY
        self.assertEqual({'Authorization': 'ApiKey %s:%s' % (MOCK_USER, MOCK_APIKEY)}, maccli.helper.http.get_auth_header())

        service.user = None
        service.apikey = MOCK_APIKEY
        self.assertEqual({}, maccli.helper.http.get_auth_header())

        service.user = MOCK_USER
        service.apikey = None
        self.assertEqual({}, maccli.helper.http.get_auth_header())

        service.user = None
        service.apikey = None
        self.assertEqual({}, maccli.helper.http.get_auth_header())
