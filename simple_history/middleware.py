from . models import HistoricalRecords
from django.utils.deprecation import MiddlewareMixin

class HistoryRequestMiddleware(MiddlewareMixin):
    """Expose request to HistoricalRecords.

    This middleware sets request as a local thread variable, making it
    available to the model-level utilities to allow tracking of the
    authenticated user making a change.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
	    HistoricalRecords.thread.request = request
	    if hasattr(HistoricalRecords.thread, 'request'):
            del HistoricalRecords.thread.request
            
	    response = self.get_response(request)
        return response
