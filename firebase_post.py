from firebase import firebase
from utils.utils import *

class FirebasePost(object):

    """
        Parameters:
         - desc (string)
         - iconUrl (string)
         - location (string)
         - salary (string)
         - title (string)
         - url (string)

        """

    def __init__(self, **kwargs):
        self.desc = kwargs.get('desc')
        self.iconUrl = kwargs.get('iconUrl')
        self.location = kwargs.get('location')
        self.salary = kwargs.get('salary')
        self.title = kwargs.get('title')
        self.url = kwargs.get('url')
    
    def administrationPost(self, name):
        firebasex = firebase.FirebaseApplication(JOLT_URL, None)
        data =  { 
            'desc': self.desc,
            'iconUrl': self.iconUrl,
            'location': self.location,
            'salary': self.salary,
            'title': self.title,
            'url': self.url
        }
        result = firebasex.put(JOLT_JOB_ADMINISTRATION_URL, name, data)
        return result
    
    def businessPost(self, name):
        firebasex = firebase.FirebaseApplication(JOLT_URL, None)
        data =  { 
            'desc': self.desc,
            'iconUrl': self.iconUrl,
            'location': self.location,
            'salary': self.salary,
            'title': self.title,
            'url': self.url
        }
        result = firebasex.put(JOLT_JOB_BUSINESS_URL, name, data)
        return result
    
    def designPost(self, name):
        firebasex = firebase.FirebaseApplication(JOLT_URL, None)
        data =  { 
            'desc': self.desc,
            'iconUrl': self.iconUrl,
            'location': self.location,
            'salary': self.salary,
            'title': self.title,
            'url': self.url
        }
        result = firebasex.put(JOLT_JOB_DESIGN_URL, name, data)
        return result
    
    def hardwarePost(self, name):
        firebasex = firebase.FirebaseApplication(JOLT_URL, None)
        data =  { 
            'desc': self.desc,
            'iconUrl': self.iconUrl,
            'location': self.location,
            'salary': self.salary,
            'title': self.title,
            'url': self.url
        }
        result = firebasex.put(JOLT_JOB_HARDWARE_URL, name, data)
        return result
    
    def hrPost(self, name):
        firebasex = firebase.FirebaseApplication(JOLT_URL, None)
        data =  { 
            'desc': self.desc,
            'iconUrl': self.iconUrl,
            'location': self.location,
            'salary': self.salary,
            'title': self.title,
            'url': self.url
        }
        result = firebasex.put(JOLT_JOB_HR_URL, name, data)
        return result
    
    def marketingPost(self, name):
        firebasex = firebase.FirebaseApplication(JOLT_URL, None)
        data =  { 
            'desc': self.desc,
            'iconUrl': self.iconUrl,
            'location': self.location,
            'salary': self.salary,
            'title': self.title,
            'url': self.url
        }
        result = firebasex.put(JOLT_JOB_MARKETING_URL, name, data)
        return result
    
    def productPost(self, name):
        firebasex = firebase.FirebaseApplication(JOLT_URL, None)
        data =  { 
            'desc': self.desc,
            'iconUrl': self.iconUrl,
            'location': self.location,
            'salary': self.salary,
            'title': self.title,
            'url': self.url
        }
        result = firebasex.put(JOLT_JOB_PRODUCT_URL, name, data)
        return result
    
    def softwarePost(self, name):
        firebasex = firebase.FirebaseApplication(JOLT_URL, None)
        data =  { 
            'desc': self.desc,
            'iconUrl': self.iconUrl,
            'location': self.location,
            'salary': self.salary,
            'title': self.title,
            'url': self.url
        }
        result = firebasex.put(JOLT_JOB_SOFTWARE_URL, name, data)
        return result