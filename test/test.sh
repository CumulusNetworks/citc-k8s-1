#
# Copyright (C) 2018 Cumulus Networks, Inc. All rights reserved
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# https://www.debian.org/legal/licenses/mit
# 
sudo apt-get install -qy python-dev libssl-dev sshpass build-essential libffi-dev
sudo pip install setuptools --upgrade
sudo pip install ansible --upgrade
rm -rf ansible-push-keys
git clone https://github.com/cumulusnetworks/ansible-push-keys
cd ansible-push-keys; cat /etc/dhcp/dhcpd.hosts | grep 'host .* {' | cut -d " " -f 2 >> hosts
cd ansible-push-keys; ansible-playbook push-keys.yml --extra-vars 'ansible_ssh_pass=CumulusLinux!' --extra-vars 'ansible_become_pass=CumulusLinux!'
rm -rf ansible-push-keys
ansible-playbook setup.yaml
