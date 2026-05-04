#qui provo delle robe
from database.DAO import DAO

allObjects = DAO.getAllNodes()
print(len(allObjects))