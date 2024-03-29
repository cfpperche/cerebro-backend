from django.test import RequestFactory, Client
from cerebromix.tenant_schemas.middleware import TenantMiddleware


class TenantRequestFactory(RequestFactory):
    tm = TenantMiddleware()

    def __init__(self, tenant, **defaults):
        super(TenantRequestFactory, self).__init__(**defaults)
        self.tenant = tenant

    def get(self, path, data={}, **extra):
        if 'HTTP_HOST' not in extra:
            extra['HTTP_HOST'] = self.tenant.domain_url

        return super(TenantRequestFactory, self).get(path, data, **extra)
        
    def post(self, path, data={}, **extra):
        if 'HTTP_HOST' not in extra:
            extra['HTTP_HOST'] = self.tenant.domain_url

        return super(TenantRequestFactory, self).post(path, data, **extra)
        

class TenantClient(Client):
    tm = TenantMiddleware()

    def __init__(self, tenant, enforce_csrf_checks=False, **defaults):
        super(TenantClient, self).__init__(enforce_csrf_checks, **defaults)
        self.tenant = tenant

    def get(self, path, data={}, **extra):
        if 'HTTP_HOST' not in extra:
            extra['HTTP_HOST'] = self.tenant.domain_url
            
        return super(TenantClient, self).get(path, data, **extra)
            
    def post(self, path, data={}, **extra):
        if 'HTTP_HOST' not in extra:
            extra['HTTP_HOST'] = self.tenant.domain_url
            
        return super(TenantClient, self).post(path, data, **extra)
