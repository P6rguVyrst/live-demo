#!/usr/bin/env bash

set -e

minikube start --cache-images -p minikube --kubernetes-version="v1.13.2" \
    --memory=8192 --cpus=4 \
    --extra-config=kubelet.authentication-token-webhook=true \
    --extra-config=kubelet.authorization-mode=Webhook \
    --extra-config=scheduler.address=0.0.0.0 \
    --extra-config=controller-manager.address=0.0.0.0 \
    --extra-config=apiserver.service-cluster-ip-range=10.96.0.0/24


minikube -p minikube addons enable kube-dns
minikube -p minikube addons enable ingress

ssh-keyscan $(minikube -p minikube ip) >> ~/.ssh/known_hosts
