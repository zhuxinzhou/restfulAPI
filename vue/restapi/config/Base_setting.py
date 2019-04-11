

AUTH_COOKIE_NAME = "FOOD"


#过滤url

INGNORE_URLS =[
    "^/user/login",
    "/api"

]


INGNORE_CHECK_LOGIN_URLS =[
    "^/static",
    "^/favicon.ico"

]
page_size = 50
page_display = 10

STATUS_MAPPING = {
    "1" :"正常",
    "0":"已删除"
}

release_version = 1


MINA_APP = {
    'appid':'wx4302ac11f53ce86a',
    'AppSecret':'70a56f851275e41489c7b93a4f70908a'
}

UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/static/upload/',
    'prefix_url':'/static/upload/'
}

APP = {
    'domain':'http://127.0.0.1:5000'
}

