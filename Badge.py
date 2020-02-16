'''
The Badge class is used for creating Badge objects which are rewarded to users.
Each badge consists of an image (path address), name, description, and a boolean indicating whether
it has been awarded.
'''
class Badge:
    def __init__(self, image, name, description, isAwarded):
        self.image = image
        self.name = name
        self.description = description
        self.isAwarded = isAwarded

    def setImage(self, newImage):
        self.image = newImage

    def setName(self, newName):
        self.name = newName

    def setDescription(self, newDescription):
        self.description = newDescription

    def setIsAwarded(self, bool1):
        if bool1:
            self.isAwarded = True
        else:
            self.isAwarded = False

    def getImage(self):
        return self.image

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description

    def getIsAwarded(self):
        return self.isAwarded


