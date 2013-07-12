import yaml
from sam import Sam

def load_sam(path='config/sam.yml'):
    '''load a Sam object from given path; has to be valid yaml'''
    with open(path) as fd:
        sam = yaml.load(fd)
    return sam 
