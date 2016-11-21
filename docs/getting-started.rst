Getting started
===============

.. include:: includes/all.rst

.. contents::
:local:


Example inventory
-----------------

To setup and configure Firejail on a given host it should be included in the
``debops_service_sentry`` Ansible inventory group:

.. code:: ini

   [debops_service_sentry]
   hostname

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

