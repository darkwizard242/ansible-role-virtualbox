import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE = 'virtualbox-6.1'
PACKAGE_BINARY = '/usr/bin/virtualbox'
DEBIAN_REPO_FILE = '/etc/apt/sources.list.d/virtualbox.list'


def test_virtualbox_package_installed(host):
    """
    Tests if virtualbox-6.1 package is installed.
    """
    assert host.package(PACKAGE).is_installed


def test_virtualbox_binary_exists(host):
    """
    Tests if virtualbox binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_virtualbox_binary_file(host):
    """
    Tests if virtualbox binary is symlink type.
    """
    assert host.file(PACKAGE_BINARY).is_symlink


def test_virtualbox_binary_which(host):
    """
    Tests the output to confirm virtualbox's binary location.
    """
    assert host.check_output('which virtualbox') == PACKAGE_BINARY


def test_virtualbox_repo_exists(host):
    """
    Tests if Debian Family repo file exists for virtualbox.
    """
    assert host.file(DEBIAN_REPO_FILE).exists


def test_virtualbox_repo_file(host):
    """
    Tests if Debian Family repo file for virtualbox if file type.
    """
    assert host.file(DEBIAN_REPO_FILE).is_file
