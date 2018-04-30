#! /bin/bash

kubectl get deployments | grep -q ubuntu1 || {
    kubectl create -f deploys1.yml
}

kubectl get deployments | grep -q ubuntu2 || {
    kubectl create -f deploys2.yml
}
