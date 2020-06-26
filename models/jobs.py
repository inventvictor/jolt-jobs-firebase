class Jobs(object):
    """
        Parameters:
         - jobTitle (string)
         - companyName (string)
         - location (string)
         - salary (string)
         - logoUrl (string)
         - jobUrl (string)

        """
    def __init__(self, **kwargs):
        self.jobTitle = kwargs.get('jobTitle')
        self.companyName = kwargs.get('companyName')
        self.location = kwargs.get('location')
        self.salary = kwargs.get('salary')
        self.logoUrl = kwargs.get('logoUrl')
        self.jobUrl = kwargs.get('jobUrl')
    
    def getJobTitle(self):
        return self.jobTitle
    
    def getCompanyName(self):
        return self.companyName
    
    def getLocation(self):
        return self.location
    
    def getSalary(self):
        return self.salary
    
    def getLogoUrl(self):
        return self.logoUrl
    
    def getJobUrl(self):
        return self.jobUrl
    
    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)

if __name__ == "__main__":
    j = Jobs(jobTitle="x", companyName="y", location="z", salary="f", logoUrl="g", jobUrl="y")
    print (j)