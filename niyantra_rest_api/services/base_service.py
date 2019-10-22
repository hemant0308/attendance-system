from sqlalchemy.orm.exc import NoResultFound

from niyantra_rest_api.exceptions import NoResourceFound

class BaseService(object):
    def __init__(self,model_class):
        self.model_class = model_class
        pass

    def set_request(self,request):
        self.request = request
        self.dbsession = request.dbsession

    def create(self,model):
        self.dbsession.add(model)
        self.dbsession.flush()
        return model

    def update(self,id, model):
        _model = self.get(id)
        self.dbsession.merge(model)
        return model

    def get(self,id,**kwargs):
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
        print(model)
        #self.dbsession.delete(model)
        self.flush()

