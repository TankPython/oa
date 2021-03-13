from django.utils.deprecation import MiddlewareMixin
import json
from common.utils import get_result


class MD1(MiddlewareMixin):


    def process_response(self, request, response):
        # 基于请求响应
        # 在视图之后
        if (json.loads(response.content.decode())).get("detail"):
            response.content = json.dumps(get_result("NoAuth")).encode()
            response.status_code = 200
        return response
