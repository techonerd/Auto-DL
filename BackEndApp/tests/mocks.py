import os
import sys

sys.path.append("..")


class MockOS:
    def mock_jwt_secret(self, mocker):
        mocker.patch.dict(os.environ, {"JWT_SECRET": "secret"})

    def mock_mongodb_uri(self, mocker):
        mocker.patch.dict(os.environ, {"MONGODB_URI": "some_uri"})


class MockUser:
    def mock_user(self):
        return {"username": "trial", "email": "trial@gmail.com"}

    def mock_none_user(self):
        return None

    def mock_wrong_user(self):
        return {"username": None, "email": None}
