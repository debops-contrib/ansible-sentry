#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Get email-addresses of all sentry users"""
import os
from ansible.module_utils.basic import *
from sentry.utils.runner import configure


def main():

    fields = {
        'config': {'default': '~./sentry', 'type': 'str'},
    }

    module = AnsibleModule(argument_spec=fields)
    os.environ['SENTRY_CONF'] = module.params['config']
    configure()
    from sentry.models import User  # noqa
    response = [x.email for x in User.objects.all()]
    module.exit_json(changed=False, emails=response)


if __name__ == '__main__':
    main()
