from flask import request

class VerifyRequest():
    @staticmethod
    def is_valid_request(request: request, expectedContentType="", requiredHeaders=[], requiredArgs=[], requiredBodyFields=[]):
        if request.content_type != expectedContentType:
            return False
        
        for header in requiredHeaders:
            if header not in request.headers:
                return False
            
        for arg in requiredArgs:
            if arg not in request.args:
                return False
        
        for field in requiredBodyFields:
            if field not in request.json:
                return False

        return True


