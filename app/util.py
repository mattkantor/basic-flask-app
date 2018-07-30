def get_domain_for_url(url):
    from urllib.parse import urlparse
    # from urlparse import urlparse  # Python 2
    parsed_uri = urlparse(url)
    result = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
    return result