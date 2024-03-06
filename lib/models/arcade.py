
from models.__init__ import CONN, CURSOR

class Arcade:

    all = []

    def __init__(self, member, tag, location):
        #this will pull the name from member
        self._member = member
        #based on membership level the person has access to 1, 2, or 3 locations
        self.location = location 
        #this will pull the membership 
        # self.tag = tag
        Arcade.add_access(self)
    
    @property
    def member(self):
        return self._member
    
    @member.setter
    def member(self, new_member):
        if not hasattr(self, "_member"):
            if type(new_member) == str:
                if 1<= len(new_member) <= 10:
                    raise ValueError("All new members must be betweeen 1 and 10 characters")
            raise TypeError("Name must be a string")
      
        self.member = new_member
    
    @property
    def tag(self):
        self.tag = self.tag
    @tag.setter
    def tag(self, new_tag):
        if isinstance(new_tag, str):
            if 3 <= len(new_tag) <= 15:
                    self._tag = new_tag
            else:
                raise ValueError("This tag must be at least 3 and 15 characters long")
        else:
            raise TypeError("tag name must be a string")

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, new_location):
        if isinstance(new_location, str):
            if 7 <= len(new_tag) <= 25:
                    self._tag = new_tag
            else:
                raise ValueError("This tag must be at least 7 and 25 characters long")
        else:
            raise TypeError("tag name must be a string")

        

    @classmethod
    def locations(cls):
        return [locale.location for locale in Locale.all]
    
    @classmethod
    def members(cls):
        return [member.members for member in Member.all]
    
    
    @classmethod
    def add_access(cls, new_access):
        cls.all.append(new_access)


    def __repr__(self):
        return f'{self.member} // {self.location}'

    @classmethod
    def create_table(cls): 
        sql = """ 
            CREATE TABLE IF NOT EXISTS arcades(
            id INTEGER PRIMARY KEY,
            member_id INTEGER,
            location TEXT
            );
            """
        CURSOR.execute(sql)
        CONN.commit()
    # database foreign keys/ refrences 

    
=======

class Arcade:
    all = []

    def __init__(self, name, location,  tag=''):
        self.name = name
        self.location = location 
        self.tag = tag
        Arcade.add_access(self)

    @classmethod
    def add_access(cls, new_access):
        cls.all.append(new_access)

    @property
    def tag(self):
        return self._tag
    
    @tag.setter
    def tag(self, new_tag):
        self._tag = new_tag
        
    @property
    def tag(self):
        return self._tag
    
    @tag.setter
    def tag(self, new_tag):
        #add logic to make sure there are no duplicate tags
        if 5 <= len(new_tag) <= 15:
            self._tag = new_tag
        else:
            raise ValueError(f'Tag {new_tag} is not between 5 and 15 characters, please enter a different tag')

