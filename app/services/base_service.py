from datetime import datetime

from sqlalchemy.orm.exc import NoResultFound

from app.exceptions import ResourceNotFound
from app.models import Trackable
from app.utils import get_user_id

class BaseService(object):
    def __init__(self,model_class):
        self.model_class = model_class
        pass

    def set_request(self,request):
        self.request = request
        self.dbsession = request.dbsession

    def create(self,model):
        if isinstance(model, Trackable):
            model.created_by = get_user_id(self.request)
            model.created_at = datetime.now()
        self.dbsession.add(model)
        self.flush()
        return model

    def update(self, id, model, **kwargs):
        _model = self.get(id,**kwargs)
        model.id = id
        if(isinstance(model, Trackable)):
            model.updated_by = get_user_id(self.request)
            model.updated_at = datetime.now()
        self.dbsession.merge(model)
        return model

    def save(self, model):
        self.dbsession.add(model)

    def get(self, id, **kwargs):
        model_class = self.model_class
        if 'model_class' in kwargs:
            model_class = kwargs['model_class']
        return self.dbsession.query(model_class).get(id)

    def all(self):
        return self.dbsession.query(self.model_class).all()

    def flush(self):
        self.dbsession.flush()

    def delete(self, id):
        model = self.get(id)
        if model is not None:
            self.dbsession.delete(model)
            self.flush()
        else:
            raise ResourceNotFound()

