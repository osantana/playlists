import os

import pytest

from playlists import PropertyListStorage


@pytest.fixture
def resources_path():
    return os.path.join(os.path.dirname(__file__), 'resources')


@pytest.fixture
def plist_xml_filename(resources_path):
    return os.path.join(resources_path, 'plist_sample.xml')


@pytest.fixture
def empty_json_filename(resources_path):
    filename = os.path.join(resources_path, 'playlists.json')

    yield filename

    if os.path.exists(filename):
        os.remove(filename)


@pytest.fixture
def plist_invalid_xml_filename(resources_path):
    return os.path.join(resources_path, 'empty.xml')


@pytest.fixture
def playlists(plist_xml_filename):
    xml = PropertyListStorage(plist_xml_filename)
    return xml.get_playlists()
