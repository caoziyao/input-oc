from . import *

session = {}
session_id = ''

# 用户类
class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.userid = ''

    @property
    def is_authenticated(self):
        """当用户登录成功后，该属性为True
        """
        return True

    @property
    def is_active(self):
        """如果该用户账号已被激活，且该用户已登录成功，则此属性为True
        """
        return True

    @property
    def is_anonymous(self):
        """是否为匿名用户（未登录用户）
        """
        return True

    def get_id(self):
        return 'id'

    @classmethod
    def get(cls, userid):
        """The function you set should take a user ID (a ``unicode``) and return a
        user object, or ``None`` if the user does not exist.
        """
        # uuid.uuid3(uuid.NAMESPACE_DNS, username) 当作 userid
        # log('get', userid)
        username = session.get(userid, '')
        data = {
            'username': username
        }
        res = dbuser.findone(data)
        if res:
            username = res.get('username', '')
            password = res.get('password', '')
            u = cls(username, password)
            u.userid = userid
            return u
        else:
            return None


# from flask_login import LoginManager
# login_manager = LoginManager()
# login_manager.user_loader()
# from flask_login import login_user

def user_loader(callback):
    '''
    This sets the callback for reloading a user from the session. The
    function you set should take a user ID (a ``unicode``) and return a
    user object, or ``None`` if the user does not exist.
    # from flask_login import LoginManager
    # login_manager = LoginManager()
    # login_manager.user_loader()
    '''
    log('call', callback)
    return callback


@user_loader
def load_user(userid):
    """
    :param uid:
    :return:
    """
    # 这里为了方便，把 username 当作 userid
    log('load_user', userid)
    return User.get(userid)


def login_required(func):
    '''
    If you decorate a view with this, it will ensure that the current user is
    logged in and authenticated before calling the actual view. (If they are
    not, it calls the :attr:`LoginManager.unauthorized` callback.) For
    example::

        @app.route('/post')
        @login_required
        def post():
            pass
    # from flask_login import login_required
    '''
    from functools import wraps
    @wraps(func)    # example.__name__ , example.__doc__
    def decorated_view(*args, **kwargs):
        # print('before login', *args)  #
        cuser = curr_user(*args)
        if cuser:
            return func(*args, **kwargs)
        else:
            log('未登录为你跳转到登录页面')
            return redirect('/login')
    return decorated_view



#: A proxy for the current user. If no user is logged in, this will be an
#: anonymous user
def curr_user(request):
    """user
    #from flask_login import current_user,
    """
    uid = request.Cookie.get('username', '')
    return User.get(uid)


# curr_user should be an instance of your `User` class
def login_user(user, remember=False, force=False, fresh=True):
    '''
    #from flask_login import login_user
    Logs a user in. You should pass the actual user object to this. If the
    user's `is_active` property is ``False``, they will not be logged in
    unless `force` is ``True``.
    '''
    global session_id
    session_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, user.username))
    user.uid = session_id
    session[session_id] = user.username

    if remember:
        session['remember'] = 'set'



def valid_login(username, password):
    """ 验证表单中提交的用户名和密码
    """
    data = {
        'username': username
    }
    res = dbuser.findone(data)
    if not res:
        raise Assistant('用户不存在')

    upasswd = res.get('password', '')
    if password != upasswd:
        raise Assistant(msg='密码错误')

    return True


def login(request):
    """ ajax 登录"""
    # headers = {'Content-Type', 'application/json'}

    try:
        data = json.loads(request.body)
        username = data.get('username', '')
        password = data.get('password', '')
        if not username or not password:
            raise Assistant(msg='请输入用户名或密码')

        # 验证表单中提交的用户名和密码
        if valid_login(username, password):
            user = User(username, password)
            login_user(user)    # 通过 login_user 方法登录用户

            r = {
                'status': 1,
                'msg': 'welcome 登录成功!'
            }
            headers = {
                'Set-Cookie': 'username={}'.format(session_id)
            }
            body = json.dumps(r)
            return http_response(body, headers)
    except Assistant as e:  # 用户名或密码错误
        body = json.dumps(e.__dict__)
        log('login', e)
        return http_response(body)
    except Exception as e: # 其他异常
        r = {
            'suatus': 0,
            'msg': ' 接口错误'
        }
        body = json.dumps(r)
        log('login', e)
        return http_response(body)


def register(request):
    """ ajax 注册"""
    # headers = {'Content-Type', 'application/json'}

    try:
        data = json.loads(request.body)
        username = data.get('username', '')
        password = data.get('password', '')
        if len(username) < 3 or len(password) < 3:
            raise Assistant(msg='用户名或密码至少3位')

        data = {
            'username': username,
            'password': password
        }
        if dbuser.findone({'username': username}):
            raise Assistant(msg='用户名已存在')

        dbuser.insert(data)
        r = {
            'status': 1,
            'msg': 'welcome 注册成功!'
        }
        body = json.dumps(r)
        return http_response(body)
    except Assistant as e:
        body = json.dumps(e.__dict__)
        return http_response(body)
    except Exception as e:
        r = {
            'suatus': 0,
            'msg': ' 接口错误'
        }
        body = json.dumps(r)
        return http_response(body)


route_ajax = {
    '/ajaxlogin': login,
    '/ajaxregister': register,
}
