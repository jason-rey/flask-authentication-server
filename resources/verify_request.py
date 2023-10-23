from flask import request

class VerifyRequest():
    @staticmethod
    def is_valid_request(request: request, requiredHeaders=[], requiredArgs=[]):
        for header in requiredHeaders:
            if header not in request.headers:
                return False
            
        for arg in requiredArgs:
            if arg not in request.args:
                return False

        return True


