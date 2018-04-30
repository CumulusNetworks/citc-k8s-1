sudo apt-get install -qy python-dev libssl-dev sshpass build-essential libffi-dev
sudo pip install setuptools --upgrade
sudo pip install ansible --upgrade
rm -rf ansible-push-keys
git clone https://github.com/cumulusnetworks/ansible-push-keys
cd ansible-push-keys; cat /etc/dhcp/dhcpd.hosts | grep 'host .* {' | cut -d " " -f 2 >> hosts
cd ansible-push-keys; ansible-playbook push-keys.yml --extra-vars 'ansible_ssh_pass=CumulusLinux!' --extra-vars 'ansible_become_pass=CumulusLinux!'
rm -rf ansible-push-keys
ansible-playbook setup.yaml
