import configparser
import os

class HarborFtpCfg():
    _instance = None
    _hasinit = False

    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._hasinit:
            cfg = configparser.ConfigParser()
            cfg.read(os.path.dirname(os.path.realpath(__file__)) + '/conf/harborftp.conf')
            # ACCOUNT
            self.ak = cfg.get("Harbor_ACCOUNT", "access_key")
            self.sk = cfg.get("Harbor_ACCOUNT", "secret_key")
            self.bucket = cfg.get("Harbor_ACCOUNT", "bucket")
            self.homedir = cfg.get("Harbor_ACCOUNT", "home_dir")

            login_users = cfg.get("FTP_ACCOUNT", "login_users")
            login_users = login_users.strip(" ").split(";")
            self.login_users = list()
            # self.login_users 的结构为 [ (user1,pass1,RW), (user2,pass2,RW) ]
            for element in login_users:
                login_user = element.split(":")
                self.login_users.append(tuple(login_user))
            self._hasinit == True
    def __str__(self):
        return "access_key: %s \n" \
               "secret_key: %s \n" \
               "bucket: %s \n" \
               "home_dir: %s \n" \
               "login_users: %s \n" \
               % (self.ak, self.sk, self.bucket, self.homedir, self.login_users)


if __name__ == '__main__':
    print(HarborFtpCfg())