# Instrumentation Demo:

## Setup your Python Django project

    pip install coderedcms
    coderedcms start instrumentation --sitename "Instrument your code." --domain demo.devs.navenio.cloud 

## Step 2: Means of deplpyment

    mkdir -p instrumentation/charts/incubator
    cd instrumentation/charts/incubator
    helm create wagtail
    cd ../../
    git commit -m "Vanilla Python project and a helm chart for deployment."
    helm upgrade demo --namespace toomas --install charts/incubator/wagtail -f values.yaml

## Start patching and deploying.

    git apply patcch/1_deployable_chart.patch
    ...# Instrumentation Demo:
