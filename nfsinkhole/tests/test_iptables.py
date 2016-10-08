import logging
from nfsinkhole.exceptions import (IPTablesError, IPTablesExists,
                                   IPTablesNotExists, SubprocessError)
from nfsinkhole.iptables import IPTablesSinkhole
from nfsinkhole.tests import TestCommon

LOG_FORMAT = ('[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)s] '
              '[%(funcName)s()] %(message)s')
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
log = logging.getLogger(__name__)


class TestIPTablesSinkhole(TestCommon):

    def test_create_drop_rule(self):

        # Bad interface
        myobj = IPTablesSinkhole(
            interface='~!@#$%^&*()',
        )
        myobj.create_drop_rule()
        self.assertRaises(IPTablesExists, myobj.create_drop_rule)

        # Success
        myobj = IPTablesSinkhole(
            interface='eth1',
        )
        myobj.create_drop_rule()

        # Exists
        self.assertRaises(IPTablesExists, myobj.create_drop_rule)

    def test_delete_drop_rule(self):

        # Bad interface
        myobj = IPTablesSinkhole(
            interface='~!@#$%^&*()',
        )
        myobj.delete_drop_rule()
        self.assertRaises(IPTablesNotExists, myobj.delete_drop_rule)

        # Success
        myobj = IPTablesSinkhole(
            interface='eth1',
        )
        myobj.delete_drop_rule()

        # Exists
        self.assertRaises(IPTablesNotExists, myobj.delete_drop_rule)

    def test_create_rules(self):

        # Success
        myobj = IPTablesSinkhole(
            interface='eth1',
            interface_addr='127.0.0.1'
        )
        myobj.create_rules()

        # Exists
        self.assertRaises(IPTablesExists, myobj.create_rules)

    def test_delete_rules(self):

        # Success
        myobj = IPTablesSinkhole(
            interface='eth1',
            interface_addr='127.0.0.1'
        )
        myobj.delete_rules()

        # Exists
        self.assertRaises(IPTablesNotExists, myobj.delete_rules)
