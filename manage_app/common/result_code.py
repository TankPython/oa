rest_code = {
    "success": {"meta": {"status": 200, "msg": "成功"}},
    "PasswordOrUsernameError": {"meta": {"status": 5000, "msg": "用户名或密码错误"}},
    "ParamsError": {"meta": {"status": 5001, "msg": "请求参数错误"}},
    "UserExits": {"meta": {"status": 5002, "msg": "用户已经存在"}},
    "NoAuth": {"meta": {"status": 5003, "msg": "没有权限操作"}},
    "NoAuthOperateSuperuser": {"meta": {"status": 5004, "msg": "禁止操作admin超级管理员"}},
}
