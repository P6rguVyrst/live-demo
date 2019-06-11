

## Prometheus:

    helm upgrade prometheus --namespace insight stable/prometheus --install -f minikube/values/prometheus/values.yaml

## Grafana:

    cat minikube/values/grafana/values.yaml | \ 
    sed "s#%%ELASTIC_USER%%#<VAR_ES_USER>#g" |
    sed "s#%%ELASTIC_SECRET%%#<VAR_ES_SECRET>#g" |
    sed "s#%%ELASTIC_URL%%#<VAR_ES_URL>#g" |
    sed "s#%%MONITORING_USER%%#<VAR_MON_USER>#g" | \
    sed "s#%%MONITORING_PASSWORD%%#<VAR_MON_PWD>#g" | \
    sed "s#%%OAUTH_ID%%#<VAR_OAUTH_ID>#g" | \
    sed "s#%%OAUTH_SECRET%%#<VAR_OAUTH_SECRET>#g" | \
    helm upgrade grafana --namespace insight --version 3.3.10 --install stable/grafana -f -
