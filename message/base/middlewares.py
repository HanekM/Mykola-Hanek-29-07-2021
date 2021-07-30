import logging


logger = logging.getLogger(__name__)


class ErrorHandler:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
    
    def process_error(self, request, exception):
        logging.error(exception)
        return request
