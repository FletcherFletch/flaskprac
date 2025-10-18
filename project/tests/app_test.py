from project.app import app 

def test_index():
    tester = app.test_client()
    response = tester.get("/", content_type="html/text")

    assert response.status_code == 200
    assert response.data == b"Hello, World!"

    # we are testing if the response that is returned has a status code of 200 and that hello world is displayed
    