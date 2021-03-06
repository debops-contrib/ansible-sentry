.. vim: foldmarker=[[[,]]]:foldmethod=marker

ansible.sentry default variables [[[
====================================

.. contents:: Sections
   :local:

.. include:: includes/all.rst


.. envvar:: sentry__base_packages [[[

List of base packages to install.
::

  sentry__base_packages:
    - 'python-setuptools'
    - 'python-pip'
    - 'python-dev'
    - 'libxslt1-dev'
    - 'gcc'
    - 'libffi-dev'
    - 'libjpeg-dev'
    - 'libxml2-dev'
    - 'libxslt-dev'
    - 'libyaml-dev'
    - 'libpq-dev'
    - '{{ "python-virtualenv"
          if (ansible_distribution_release in [ "wheezy", "precise" ])
          else "virtualenv" }}'

                                                                     # ]]]

.. envvar:: sentry__packages [[[

List of additional packages to install.
::

  sentry__packages: []

                                                                     # ]]]

.. envvar:: sentry__version [[[

The version of sentry that will be used. sentry 8.10.0 needs cmake from stretch.
::

  sentry__version: '8.8.0'

                                                                     # ]]]

.. envvar:: sentry__domain [[[

The default domain used in different places of the role.
::

  sentry__domain: '{{ ansible_domain if ansible_domain else ansible_hostname }}'

                                                                     # ]]]

.. envvar:: sentry__fqdn [[[

The Fully Qualified Domain Name of Sentry.
::

  sentry__fqdn: '{{ "sentry." + sentry__domain }}'

                                                                     # ]]]

Application user, group, home [[[
---------------------------------

.. envvar:: sentry__user [[[

Name of the UNIX system account used to manage sentry.
::

  sentry__user: 'sentry'

                                                                     # ]]]

.. envvar:: sentry__group [[[

Name of the UNIX primary group used to manage sentry.
::

  sentry__group: 'sentry'

                                                                     # ]]]

.. envvar:: sentry__shell [[[

The default shell set on the sentry account.
::

  sentry__shell: '/usr/sbin/nologin'
                                                                     # ]]]
                                                                     # ]]]

Directory paths [[[
-------------------

.. envvar:: sentry__home [[[

The sentry account home directory.
::

  sentry__home: '{{ (ansible_local.root.home
                     if (ansible_local|d() and ansible_local.root|d() and
                         ansible_local.root.home|d())
                     else "/var/local") + "/" + sentry__user }}'

                                                                     # ]]]

.. envvar:: sentry__lib [[[

Directory where the sentry application directory is located.
::

  sentry__lib: '{{ (ansible_local.root.lib
                    if (ansible_local|d() and ansible_local.root|d() and
                        ansible_local.root.lib|d())
                    else "/usr/local/lib") + "/" + sentry__user }}'

                                                                     # ]]]

.. envvar:: sentry__config [[[

Directory where the sentry config files are located.
::

  sentry__config: '/etc/sentry'
                                                                     # ]]]
                                                                     # ]]]

Python virtualenv configuration [[[
-----------------------------------

.. envvar:: sentry__virtualenv [[[

Path where the sentry ``virtualenv`` directory will be stored.
::

  sentry__virtualenv: '{{ sentry__lib + "/virtualenv" }}'

                                                                     # ]]]

.. envvar:: sentry__virtualenv_env_path [[[

The contents of the ``$PATH`` environment variable set for the Ansible tasks
which are executed inside of the sentry Python environment.
::

  sentry__virtualenv_env_path: '{{ sentry__virtualenv }}/bin:/usr/local/bin:/usr/bin:/bin'

                                                                     # ]]]

.. envvar:: sentry__virtualenv_pip_packages [[[

List of additional Python modules installed inside of the sentry
``virtualenv`` environment. See :ref:`sentry__ref_virtualenv_pip_packages`
for more details.
::

  sentry__virtualenv_pip_packages:
    - name: 'sentry'
      version: '{{ sentry__version }}'
                                                                     # ]]]
                                                                     # ]]]

.. envvar:: sentry__database_user [[[

Name of the PostgreSQL user used by sentry.
::

  sentry__database_user: 'sentry'

                                                                     # ]]]

.. envvar:: sentry__database_name [[[

# Name of the PostgreSQL database used by sentry.
::

  sentry__database_name: 'sentry'

                                                                     # ]]]

.. envvar:: sentry__postgresql_user_role [[[

Configure settings of the postgresql role
::

  sentry__postgresql_user_role:
    name: '{{ sentry__database_user }}'
    flags:
      - 'NOSUPERUSER'
      - 'NOCREATEROLE'
      - 'NOCREATEDB'
      - 'NOINHERIT'
      - 'NOREPLICATION'
      - 'LOGIN'
    db: '{{ sentry__database_name }}'

                                                                     # ]]]

.. envvar:: sentry__postgresql_roles [[[

FIXME: Describe what this variable is doing.
::

  sentry__postgresql_roles:
    - '{{ sentry__postgresql_user_role }}'  # Password is not passed directly - it will be read from the file

                                                                     # ]]]

.. envvar:: sentry__postgresql_database [[[

The postgresql database name and owner used by sentry
::

  sentry__postgresql_database:
    name: '{{ sentry__database_name }}'
    owner: '{{ sentry__database_user }}'

                                                                     # ]]]

.. envvar:: sentry__superusers [[[

Name of the sentry superuser
::

  sentry__superusers: '{{ lookup("template", "lookup/sentry__config_admins.j2") | from_yaml }}'

                                                                     # ]]]

.. envvar:: sentry__superuser_password_length [[[

Length of the superuser password
::

  sentry__superuser_password_length: '32'

                                                                     # ]]]

.. envvar:: sentry__nginx_upstream [[[

Nginx upstream configuration
::

  sentry__nginx_upstream:
    name: 'sentry'
    enabled: True
    type: 'default'
    server: ['[::1]:9000']

                                                                     # ]]]

.. envvar:: sentry__nginx_web_server [[[

Nginx vhost configuration
::

  sentry__nginx_web_server:
    enabled: True
    name: '{{ sentry__domain }}'
    welcome: False
    ssl: True
    acme: False
    root: False
    index: False
    favicon: True
    redirect_to_ssl: True
    location:
      '/': |
        include     uwsgi_params;
        uwsgi_pass  sentry;


]]]
]]]
