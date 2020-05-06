class Bank:
    def __init__(self):
        self.branch = [1111, 2222, 3333,4444]
        self.client = []
        self.account = []

    def insert_client(self, client):
        self.client.append(client)

    def insert_account(self, account):
        self.account.append(account)

    def _validation(self, client):

        if client not in self.client:
            return False

        if client.account not in self.account:
            return False

        if client.account.branch not in self.branch:
            return False

        return True