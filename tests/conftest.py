import pytest


@pytest.fixture()
def config_json():
    return {
        "status": "1",
        "commands": [
            {
                "name": "1st",
                "lambda": "first-lambda"
            },
            {
                "name": "2nd",
                "lambda": "second-lambda"
            },
            {
                "name": "3rd",
                "lambda": "third-lambda"
            }]
        }
