import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_googlechrome_package_installed(host):
    assert host.package("virtualbox-6.1").is_installed


def test_googlechrome_binary_exists(host):
    assert host.file('/usr/bin/virtualbox').exists


def test_googlechrome_binary_symlink(host):
    assert host.file('/usr/bin/virtualbox').is_symlink


def test_googlechrome_binary_which(host):
    assert host.check_output('which virtualbox') == '/usr/bin/virtualbox'


def test_googlechrome_repo_exists(host):
    assert host.file('/etc/apt/sources.list.d/virtualbox.list').exists


def test_googlechrome_repo_file(host):
    assert host.file('/etc/apt/sources.list.d/virtualbox.list').is_file
