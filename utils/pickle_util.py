import pickle
from config import *
def serialize(data_obj, file_path= "data/emails.obj"):


    # obj = {'Python': 3, 'KDE': 5, 'Windows': 10}

    fileObj = open(file_path, 'wb')
    pickle.dump(data_obj, fileObj)
    fileObj.close()

def deserialize(file_path= "data/emails.obj"):

    fileObj = open(file_path, 'rb')
    data_obj = pickle.load(fileObj)
    fileObj.close()
    return data_obj

if __name__ == '__main__':
    base_dir = Config.EMAIL_CATEGORY_DATA
    import os
    print(os.path.join(base_dir, "emails.obj"))
    data_obj = deserialize(os.path.join(base_dir, "emails.obj"))
    print(data_obj['236455'])
