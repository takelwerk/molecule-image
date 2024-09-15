import os
import takeltest

testinfra_hosts = [takeltest.hosts()[0]]


def test_image_meta_env_exists(image_meta_data):
    assert image_meta_data['Config']['Env'] is not None


def test_image_meta_cmd(testvars, image_meta_data):
    image = os.environ.get('TAKELAGE_PROJECT_IMG')
    if 'command' in testvars['project']['images'][image]:
        expected = testvars['project']['images'][image]['command']
    else:
        expected = ['/bin/sh', '-c', '/usr/bin/tail -f /dev/null']
    assert expected == image_meta_data['Config']['Cmd']


def test_image_meta_work_dir(image_meta_data):
    assert '/root' == image_meta_data['Config']['WorkingDir']
