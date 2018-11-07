import argparse
import os


class WhereAction(argparse.Action):

    def __init__(self, option_strings, dest, nargs=None, **kwargs):
        super(WhereAction, self).__init__(option_strings, dest, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        where = []
        for value in values.split(','):
            key, value = value.split(':')
            where.append({'key': key, 'value': value})
        setattr(namespace, self.dest, where)


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--dci-cs-url',
        dest='dci_cs_url',
        default=os.environ.get('DCI_CS_URL', 'https://api.distributed-ci.io')
    )
    parser.add_argument(
        '--dci-login',
        dest='dci_login',
        default=os.environ.get('DCI_LOGIN')
    )
    parser.add_argument(
        '--dci-password',
        dest='dci_password',
        default=os.environ.get('DCI_PASSWORD')
    )
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--limit', type=int, default=10)
    parser.add_argument('--sort')
    parser.add_argument('--where', action=WhereAction, default=[])
    parser.add_argument('resource', nargs='?', default='users')
    parser.add_argument('action', nargs='?', default='list')
    # https://stackoverflow.com/questions/37367331/is-it-possible-to-use-argparse-to-capture-an-arbitrary-set-of-optional-arguments
    parsed, unknown = parser.parse_known_args()
    parsed = vars(parsed)
    parsed['action_args'] = {}
    for arg in unknown:
        if arg.startswith("--"):
            k, v = arg[2:].split('=')
            parsed['action_args'][k] = v
    parsed['bob'] = 1
    return parsed
