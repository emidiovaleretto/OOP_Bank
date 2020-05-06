from datetime import datetime
from pytz import timezone


class RealTime:

    @staticmethod
    def realtime():
        actual = datetime.now()
        irish_time_fuse = timezone('Eire')
        time_actual = actual.astimezone(irish_time_fuse)
        date = time_actual.strftime('%A %d/%m/%Y - %H:%M:%S')
        return date

