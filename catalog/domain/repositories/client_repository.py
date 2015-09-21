from catalog.domain.entities.client import Client


class ClientRepository(object):

    def get(self, client_id):
        # FAKE CLIENT
        client = Client('Fake Client')
        client.id = 1
        return client
