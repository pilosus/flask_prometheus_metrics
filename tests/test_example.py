def test_endpoint_index(app, client):
    with app.test_request_context():
        response = client.get("/")
        assert b"Test" in response.data


def test_metric_app_version_info(app, client):
    with app.test_request_context():
        response = client.get("/metrics")
        assert b"app_version_info" in response.data


def test_metric_app_request_latency_seconds(app, client):
    with app.test_request_context():
        response = client.get("/metrics")
        assert b"app_request_latency_seconds" in response.data


def test_metric_app_request_count(app, client):
    with app.test_request_context():
        response = client.get("/metrics")
        assert b"app_request_count" in response.data


def test_standard_metrics(app, client):
    with app.test_request_context():
        response = client.get("/metrics")
        assert b"python_gc_objects_collected_total" in response.data
        assert b"python_gc_objects_uncollectable_total" in response.data
        assert b"python_gc_collections_total" in response.data
        assert b"python_info" in response.data
        assert b"process_virtual_memory_bytes" in response.data
        assert b"process_resident_memory_bytes" in response.data
        assert b"process_start_time_seconds" in response.data
        assert b"process_cpu_seconds_total" in response.data
        assert b"process_open_fds" in response.data
        assert b"process_max_fds" in response.data
