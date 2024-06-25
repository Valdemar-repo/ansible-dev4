"""testinfra for HOST"""

import pytest


def test_file_var_exists(host):
    """Checking file var exists."""
    assert host.file('/etc/var').exists


def test_file_var_content(host):
    """Checking file var content."""
    assert host.file('/etc/var').content_string == "something"


def test_file_var_owner_and_group(host):
    """Checking file var owner and group."""
    assert host.file('/etc/var').user == 'root'
    assert host.file('/etc/var').group == 'root'


def test_file_var_mode(host):
    """Checking file var mode."""
    assert host.file('/etc/var').mode == 0o777
