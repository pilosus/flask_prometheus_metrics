import time

from flask import request
from prometheus_client import Counter, Histogram, Info

#
# Metrics registration
#


METRICS_REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds", "Application Request Latency", ["method", "endpoint"]
)

METRICS_REQUEST_COUNT = Counter(
    "app_request_count",
    "Application Request Count",
    ["method", "endpoint", "http_status"],
)

METRICS_INFO = Info("app_version", "Application Version")


#
# Request callbacks
#


def before_request():
    """
    Get start time of a request
    """
    request._prometheus_metrics_request_start_time = time.time()


def after_request(response):
    """
    Register Prometheus metrics after each request
    """
    request_latency = time.time() - request._prometheus_metrics_request_start_time
    METRICS_REQUEST_LATENCY.labels(request.method, request.path).observe(
        request_latency
    )
    METRICS_REQUEST_COUNT.labels(
        request.method, request.path, response.status_code
    ).inc()
    return response


def register_metrics(app, app_version=None, app_config=None):
    """
    Register metrics middlewares

    Use in your application factory (i.e. create_app):
    register_middlewares(app, settings["version"], settings["config"])

    Flask application can register more than one before_request/after_request.
    Beware! Before/after request callback stored internally in a dictionary.
    Before CPython 3.6 dictionaries didn't guarantee keys order, so callbacks
    could be executed in arbitrary order.
    """
    app.before_request(before_request)
    app.after_request(after_request)
    METRICS_INFO.info({"version": app_version, "config": app_config})
