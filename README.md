# Kubernetes for Cumulus in the Cloud

This repository is used to configure a reference topology with Kubernetes for Cumulus-in-the-Cloud deployment.

## Network Architecture

There are two physical networks in this system, one is an out-of-band network used stictly for provisioning and low level operations.  The other is a high speed, fully redundant data plane IP fabric built using BGP unnumbered; each node is dual stack, addressable with IPv4 and IPv6.

This environment uses FRRouting from HostPack for host L3 peering with the data plane network and the NetQ host agents for host visibility. 

## Kubernetes Environment

Kubernetes is deployed on four functional Ubuntu 16.04 nodes.  The master is server01 with server02-server04 acting as worker nodes.  Flannel ( and https://github.com/coreos/flannel) provides the CNI and IPAM for this deployment.  The environment comes up with a demo "application" consisting of two containsers being deployed with with five instances.

## UIs
Besides console/ssh access into the oob-mgmt-server, the environment exports two web based UIs: NetQ Telemetry Server and the Kubernetes dashboard.

## Using
The system is deployed on a Cumulus reference topology (typically Cumulus In The Cloud) with...
```
ansible-playbook setup.yaml
```
and the UIs are accessed at the Telemetry Server's (jumpbox) IP adderess at...

* __NetQ__ : http://IP:9000 (user/password = admin/CumulusNetQ!)

* __Kubernetes__ : http://IP:8001/api/v1/namespaces/kube-system/services/https:kubernetes-dashboard:/proxy/ (SKIP authentication)

## Additional References

Here are pointers to the Kubernetes documentation that were permanently in my browser while I created the deployment...

* https://kubernetes.io/docs/setup/independent/install-kubeadm/
* https://kubernetes.io/docs/setup/cri/
* https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/
* https://kubernetes.io/docs/reference/kubectl/overview/
* https://kubernetes.io/docs/setup/independent/create-cluster-kubeadm/#tabs-pod-install-1
* https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/
