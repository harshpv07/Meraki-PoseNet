import urllib


class AsyncCamera:
    def __init__(self, session):
        super().__init__()
        self._session = session


def getDeviceCameraVideoLink(self, serial: str, **kwargs):

        kwargs.update(locals())

        metadata = {
            'tags': ['camera', 'configure', 'videoLink'],
            'operation': 'getDeviceCameraVideoLink'
        }
        serial = urllib.parse.quote(str(serial), safe='')
        resource = f'/devices/{serial}/camera/videoLink'

        query_params = ['timestamp', ]
        params = {k.strip(): v for k, v in kwargs.items() if k.strip() in query_params}

        return self._session.get(metadata, resource, params)