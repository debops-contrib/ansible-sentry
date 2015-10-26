# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "jwd/debian-7.9.0-amd64"
  config.ssh.insert_key = false

  config.vm.provider :virtualbox do |v|
    v.name = "sentry"
    v.memory = 512
    v.cpus = 1
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--ioapic", "on"]
  end

  config.vm.hostname = "sentry"
  config.vm.network :private_network, ip: "192.168.100.100"

  # Set the name of the VM. See: http://stackoverflow.com/a/17864388/100134
  config.vm.define :sentry do |sentry|
  end

  # Ansible provisioner.
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "provisioning/playbook.yml"
    ansible.inventory_path = "provisioning/inventory"
    ansible.sudo = true
  end

end
