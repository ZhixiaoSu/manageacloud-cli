import unittest, sys, StringIO
import mock
import cli.mac_cli
from mock_data import *


class AuthTestCase(unittest.TestCase):

    @mock.patch('cli.command_cli.login')
    def test_dispatch_cmds_login(self, mock):
        args = Mock_args('login', None)
        cli.mac_cli.dispatch_cmds(args)
        self.assertTrue(mock.called)

    @mock.patch('cli.command_cli.instance_create')
    def test_dispatch_cmds_create(self, mock):
        args = MockInstanceCreate_args('instance', 'create')
        cli.mac_cli.dispatch_cmds(args)
        self.assertTrue(mock.called)

    @mock.patch('cli.command_cli.instance_destroy_help')
    def test_dispatch_cmds_destroy_help(self, mock):
        args = MockInstanceDestroy_args('instance', 'destroy', None, None)
        cli.mac_cli.dispatch_cmds(args)
        self.assertTrue(mock.called)

    @mock.patch('cli.command_cli.instance_list')
    def test_dispatch_cmds_list(self, mock):
        args = Mock_args('instance', 'list')
        cli.mac_cli.dispatch_cmds(args)
        self.assertTrue(mock.called)

    @mock.patch('cli.command_cli.instance_ssh_help')
    def test_dispatch_cmds_ssh_help(self, mock):
        args = MockInstanceSSH_args('instance', 'ssh', None, None)
        cli.mac_cli.dispatch_cmds(args)
        self.assertTrue(mock.called)

    @mock.patch('cli.command_cli.instance_ssh')
    def test_dispatch_cmds_ssh_help(self, mock):
        args = MockInstanceSSH_args('instance', 'ssh', 'name', 'id')
        cli.mac_cli.dispatch_cmds(args)
        self.assertTrue(mock.called)

    @mock.patch('cli.command_cli.configuration_list')
    def test_dispatch_cmds_configuration_list(self, mock):
        args = Mock_args('configuration', 'list')
        cli.mac_cli.dispatch_cmds(args)
        self.assertTrue(mock.called)

    @mock.patch('cli.command_cli.configuration_search')
    def test_dispatch_cmds_configuration_Search(self, mock):
        args = MockConfiguration_Args('configuration', 'search', None, None)
        cli.mac_cli.dispatch_cmds(args)
        self.assertTrue(mock.called)