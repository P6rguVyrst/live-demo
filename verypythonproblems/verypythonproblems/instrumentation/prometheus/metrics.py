from prometheus_client import Gauge

"""
Prometheus Business Metrics instrumentation.
Reference: https://github.com/prometheus/client_python
"""


class ModelsGauges:
    """Monitoring definitions for Prometheus data format."""

    django_model_objects = Gauge(
        "django_model_count_total", "model label objects in database.", ["model"]
    )
