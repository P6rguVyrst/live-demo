# Instrumentation Demo:

## *NB! If you are trying to run this demo, tha patches won't work if you don't have docker images present on your local machine.*

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
