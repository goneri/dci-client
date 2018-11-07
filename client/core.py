import sys
import types

import dci_lite.client
from client.cli import parse_args



def main(args=sys.argv[1:]):
    args = parse_args(args)

    c = dci_lite.client.DCIClient.for_user(dci_login=args['dci_login'], dci_password=args['dci_password'], dci_cs_url=args['dci_cs_url'])

    resource = getattr(c, args['resource'])
    action = getattr(resource, args['action'])

    ret = action(**args['action_args'])
    if isinstance(ret, types.GeneratorType):
        for i in ret:
            print(i)
    else:
        print(ret)

