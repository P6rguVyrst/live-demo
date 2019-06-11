#!/usr/bin/env bash

set -e

minikube -p minikube stop
minikube -p minikube delete
