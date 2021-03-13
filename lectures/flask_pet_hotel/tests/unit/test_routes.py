def test_app(app):
    resp = app.get('/')
    assert resp.status_code == 200
