from time import sleep


class Log:

    @staticmethod
    def write(msg):
        with open('bank_log.log', 'a+') as file:
            file.write(msg)
            file.write('\n')

    def log_info(self, msg):
        self.write(f'Log: {msg}')
        sleep(2)
        print(msg)

    def log_error(self, msg):
        self.write(f'Error: {msg}')
        sleep(2)
        print(msg)