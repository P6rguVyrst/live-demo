from .prometheus.monitor import models_gauge_monitor
import django_prometheus


def prometheus_monitor(request):
    models_gauge_monitor()
    return django_prometheus.exports.ExportToDjangoView(request)
