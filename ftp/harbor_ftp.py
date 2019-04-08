import os
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from harbor_file_system import HarborFileSystem
from harbor_conf import HarborFtpCfg
from harbor_auth import HarborAuthorizer
 
def main():
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = HarborAuthorizer()
    # authorizer = DummyAuthorizer()

    for login_user, login_password, permission in HarborFtpCfg().login_users:
        perm = ""
        if "R" in permission:
            perm = perm + "elr"
        if "W" in permission:
            perm = perm + "adfmwMT"
        authorizer.add_user(login_user, login_password, HarborFtpCfg().homedir, perm=perm)
 
    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    # authorizer.add_user('user', '12345', '/home/ftp', perm='elradfmwM')
    # authorizer.add_anonymous('/root/ftp/')
 
    # Instantiate FTP handler class
    handler = FTPHandler
    handler.abstracted_fs = HarborFileSystem
    handler.authorizer = authorizer
 
    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."
 
    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    #handler.masquerade_address = '151.25.42.11'
    #handler.passive_ports = range(60000, 65535)
 
    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ('0.0.0.0', 2121)
    server = FTPServer(address, handler)
 
    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5
 
    # start ftp server
    server.serve_forever()
 
if __name__ == '__main__':
    main()
