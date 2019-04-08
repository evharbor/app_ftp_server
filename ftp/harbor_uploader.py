#from utils import FifoBuffer
import os

class Uploader(object):
    def __init__(self, bucket_name, ftp_path, client):
        self.bucket_name = bucket_name
        self.name = os.path.basename(ftp_path)
        self.ftp_path = ftp_path
        self.client = client
        self.closed = False
        #self.buffer = FifoBuffer()

    def write(self, data):
        path = './download_temp/' + os.path.basename(self.ftp_path)
        f = open(path, 'wb')
        f.write(data)
        f.close()
        ok, offset, msg = self.client.put_object(bucket_name=self.bucket_name, obj_name=self.ftp_path, filename=path)
        os.remove(path)
        return len(data)

    def close(self):
        self.closed = True



