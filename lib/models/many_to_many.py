class Local:
    def __init__(self, location):
        self.location = location

    @property
    def location(self):
        return self._location

    @location.setter 
    def location(self, new_location):
         if not hasattr(self, "_location"):
             self._location = new_location

class Player:
    def __init__(self, name, tag, membership):
        self.name = name
        self.tag = tag
        self.membership = membership

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if not hasattr(self, "_name"):
            self._name = new_name

    @property
    def tag(self):
        return self._tag
    
    @tag.setter
    def tag(self, new_tag):
        #logic to make sure there are no duplicate tags
        if 5 <= len(new_tag) <= 15:
            self._tag = new_tag
        else:
            raise ValueError(f'Tag {new_tag} is not between 5 and 15 characters, please enter a different tag')
        
    @property
    def membership(self):
        return self._membership
    
    @membership.setter
    def membership(self, new_membership):
        #make sure memberhsip level is 1,2, or 3
        if new_membership == 1 or new_membership == 2 or new_membership == 3:
            self._membership = new_membership
        else:
            raise ValueError("Please input a valid membership level of 1, 2, or 3")


        

class Arcade:
    def __init__(self, name, location, member):
        self.name = name
        self.location = location 
        self.member = member
        
