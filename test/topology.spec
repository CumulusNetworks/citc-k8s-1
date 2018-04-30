
vm oob-mgmt-server netq-1.3.0 2 10 40
vm leaf01 cumulus-vx-3.5.3 1 2 2
vm leaf02 cumulus-vx-3.5.3 1 2 2
vm leaf03 cumulus-vx-3.5.3 1 2 2
vm leaf04 cumulus-vx-3.5.3 1 2 2
vm spine01 cumulus-vx-3.5.3 1 2 2
vm spine02 cumulus-vx-3.5.3 1 2 2
vm server01 ubuntu-16.04 2 8 4
vm server02 ubuntu-16.04 2 4 4
vm server03 ubuntu-16.04 2 4 4
vm server04 ubuntu-16.04 2 4 4

network oob-mgmt-server eth0 10.255.0.1 255.255.0.0 public
service oob-mgmt-server ssh eth0 22 TCP public
service oob-mgmt-server netq eth0 9000 TCP public
service oob-mgmt-server dashboard eth0 8001 TCP public

network oob-mgmt-server eth1 192.168.0.254 255.255.0.0
network leaf01 eth0 192.168.0.11 255.255.0.0
network leaf02 eth0 192.168.0.12 255.255.0.0
network leaf03 eth0 192.168.0.13 255.255.0.0
network leaf04 eth0 192.168.0.14 255.255.0.0
network spine01 eth0 192.168.0.21 255.255.0.0
network spine02 eth0 192.168.0.22 255.255.0.0
network server01 eth0 192.168.0.31 255.255.0.0
network server02 eth0 192.168.0.32 255.255.0.0
network server03 eth0 192.168.0.33 255.255.0.0
network server04 eth0 192.168.0.34 255.255.0.0

autoconfig oob-mgmt-server

 connect leaf01 swp51 spine01 swp1
 connect leaf02 swp51 spine01 swp2
 connect leaf03 swp51 spine01 swp3
 connect leaf04 swp51 spine01 swp4
 connect leaf01 swp52 spine02 swp1
 connect leaf02 swp52 spine02 swp2
 connect leaf03 swp52 spine02 swp3
 connect leaf04 swp52 spine02 swp4
 connect leaf01 swp49 leaf02 swp49
 connect leaf01 swp50 leaf02 swp50
 connect leaf03 swp49 leaf04 swp49
 connect leaf03 swp50 leaf04 swp50
 connect spine01 swp31 spine02 swp31
 connect spine01 swp32 spine02 swp32
 connect server01 eth1 leaf01 swp1
 connect server01 eth2 leaf02 swp1
 connect server02 eth1 leaf01 swp2
 connect server02 eth2 leaf02 swp2
 connect server03 eth1 leaf03 swp1
 connect server03 eth2 leaf04 swp1
 connect server04 eth1 leaf03 swp2
 connect server04 eth2 leaf04 swp2
 connect leaf01 swp44 oob-mgmt-server eth2
 connect leaf02 swp44 oob-mgmt-server eth3
 connect leaf01 swp45 leaf01 swp46
 connect leaf01 swp47 leaf01 swp48
 connect leaf02 swp45 leaf02 swp46
 connect leaf02 swp47 leaf02 swp48
 connect leaf03 swp45 leaf03 swp46
 connect leaf03 swp47 leaf03 swp48
 connect leaf04 swp45 leaf04 swp46
 connect leaf04 swp47 leaf04 swp48
