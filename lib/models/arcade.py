from models.__init__ import CONN, CURSOR

class Arcade:

    all = []

    def __init__(self, member, location):
        #this will pull the name from member
        self.member = member
        #based on membership level the person has access to 1, 2, or 3 locations
        self.location = location 
        #this will pull the membership 
        # self.tag = tag
        Arcade.add_access(self)

    @classmethod
    def add_new_location(cls, new_instance):
        cls.all.append(new_instance)

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
    def location(self):
        return self._location
    
    @location.setter
    def location(self, new_location):
        if isinstance(new_location, str):
            if 3 <= len(new_tag) <= 25:
                    self._tag = new_tag
            else:
                raise ValueError("This location must be at least 7 and 25 characters long")
        else:
            raise TypeError("location name must be a string")

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

Arcade.create_table()
    # database foreign keys/ references 

