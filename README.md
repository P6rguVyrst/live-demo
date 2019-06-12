# Instrumentation Demo:

## *NB! This is the end result of the demo, if you want to follow through the steps, you might want to use master branch.*

## Install Prometheus:

    helm upgrade prometheus --namespace insight stable/prometheus --install -f infra/minikube/values/prometheus/values.yaml

## Install Grafana

    cat minikube/values/grafana/values.yaml | \
    sed "s#%%ELASTIC_USER%%#<VARIABLE>#g" | \
    sed "s#%%ELASTIC_SECRET%%#<VARIABLE>#g" | \
    sed "s#%%ELASTIC_URL%%#<VARIABLE>#g" | \
    sed "s#%%MONITORING_USER%%#<VARIABLE>#g" | \
    sed "s#%%MONITORING_PASSWORD%%#<VARIABLE>#g" | \
    sed "s#%%OAUTH_ID%%#<VARIABLE>#g" | \
    sed "s#%%OAUTH_SECRET%%#<VARIABLE>#g" | \
    helm upgrade grafana --namespace insight --version 3.3.10 --install stable/grafana -f -


## Setup your Python Django project

    pip install coderedcms
    coderedcms start verypythonproblems --sitename "Very Python Problems" --domain demo.verypythonproblems.com
    cd verypythonproblems/

## Step 2: Means of deplpyment

    mkdir -p charts/incubator
    cd charts/incubator
    helm create wagtail
    cd ../../
    helm upgrade demo --namespace london --install charts/incubator/wagtail

## Start patching and deploying.

    git apply patcch/1_deployable_project.patch
    ...

## Step 3: Means of deploying OUR code (v0.0.3 - v0.0.8)

    helm upgrade demo --namespace london --install charts/incubator/wagtail -f verypythonproblems/values.yaml

## Step 4: Means of hiding secrets (v.0.0.9 - current)

    cat values.yaml | sed "s#%%SENTRY_DSN%%#<VAR_SENTRY_DSN>#g" | \
    helm upgrade demo --namespace london --install charts/incubator/wagtail -f -
