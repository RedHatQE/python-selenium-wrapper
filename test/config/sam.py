from yaml import YAMLObject

class Sam(YAMLObject):
    yaml_tag = u'!Sam'
    '''magical Sam config representation'''

    def __init__(self, url=None, username=None, password=None):
        self.url = url
        self.username = username
        self.password = password

    def __repr__(self):
        return "%s(url=%r, username=%r, password=%r)" % (
            self.__class__.__name__,
            self.url,
            self.username,
            self.password
        ) 

    
