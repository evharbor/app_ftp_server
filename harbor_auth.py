from harbor_conf import HarborFtpCfg
from pyftpdlib.authorizers import DummyAuthorizer, AuthenticationFailed

class HarborAuthorizer(DummyAuthorizer):
    '''
    def __init__(self, *args, **kwargs):
        DummyAuthorizer.__init__(self, *args, **kwargs)
    '''
    def validate_authentication(self, user_name, password, handler):
        for login_user_name, login_password, login_permission in HarborFtpCfg().login_users:
            if user_name == login_user_name and password == login_password:
                return True

        raise AuthenticationFailed