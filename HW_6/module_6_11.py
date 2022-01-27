def get_credentials_users(path):
    r=[]
    with open(path,'rb') as f:
      for el in f.readlines():
        r+=[el.decode().replace('\n','')]
    return r