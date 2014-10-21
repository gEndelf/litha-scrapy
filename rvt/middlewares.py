from rvt.settings import HTTP_PROXY


class ProxyMiddleware(object):

    def process_request(self, request, spider):
        if HTTP_PROXY:
            request.meta['proxy'] = HTTP_PROXY
