Getting started
===============

.. include:: includes/all.rst

.. contents::
:local:


Example inventory
-----------------

To setup and configure Sentry (version 8.8.0) on a given host it should be included in the
``debops_service_sentry`` Ansible inventory group:

.. code:: ini

   [debops_service_sentry]
   hostname

Additional more services are needed on the same machine or remote:

.. code:: ini

    [debops_service_postgresql_server]
    hostname

    [debops_service_redis]
    hostname

Example inventory for Sentry version 8.10
-----------------------------------------

Sentry version 8.10 requires CMake 3.4.3+, which is only available in Debian
Testing. This extra overrides can be done to install Sentry 8.10:

.. code:: ini

    [debops_service_apt]
    hostname

    [debops_service_apt_preferences]
    hostname

And in the hostname (e.g. host_vars/hostname/sentry.yml):

.. code:: ini

    sentry__packages:
      - 'cmake'

    sentry__version: '8.10.0'

    apt_preferences__host_list:
      - package: 'cmake'
        by_role: 'debops.sentry'
        suffix: '_Debian'
        raw: |
          Explanation: Install cmake from testing. Sentry 8.10.x needs symsynd which needs CMake 3.4.3+
          Package: cmake
          Pin: release o=Debian,n=stretch
          Pin-Priority: 500

    apt__host_sources:
      - uri:        'http://httpredir.debian.org/debian'
        comment:    'Debian Stretch repository'
        type:       'deb'
        suite:      'stretch'
        components: 'main'
        distribution: 'Debian'


Example playbook
----------------

Here's an example playbook that uses the ``debops-contrib.sentry`` role:

.. literalinclude:: playbooks/sentry.yml
:language: yaml

    This playbooks is shipped with this role under
:file:`./docs/playbooks/sentry.yml` from which you can symlink it to your
playbook directory.
In case you use multiple `DebOps Contrib`_ roles, consider using the
`DebOps Contrib playbooks`_.
