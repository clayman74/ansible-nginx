import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_exporter_ready(host):
    cmd = host.run("curl -LI 172.17.0.2:3093/metrics -o /dev/null -w '%{http_code}\n' -s")  # noqa

    assert cmd.stdout == '200\n'
