import logging

class BaseService():
    def __init__(self,session):
        self.session=session
        self.logger=logging.getLogger('tornado.application')