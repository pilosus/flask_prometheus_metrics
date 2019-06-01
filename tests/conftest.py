import pytest

from flask_prometheus_metrics.example import CONFIG, create_app, create_dispatcher


def pytest_make_parametrize_id(config, val, argname):
    """
    Prettify output for parametrized tests
    """
    if isinstance(val, dict):
        return "{}({})".format(
            argname, ", ".join("{}={}".format(k, v) for k, v in val.items())
        )


@pytest.fixture(scope="module", autouse=True)
def app(request):
    """
    Return Flask Application with testing settings
    """
    app = create_app(CONFIG)
    # See https://stackoverflow.com/a/36222848/4241180
    app.wsgi_app = create_dispatcher()
    app_context = app.app_context()
    app_context.push()
    app.testing = True

    yield app


@pytest.fixture
def client(app):
    """
    Return Flask Testing Client
    """
    yield app.test_client()
