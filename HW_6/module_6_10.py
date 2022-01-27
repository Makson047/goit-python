def save_credentials_users(path, users_info):
    r=[]
    for key, val in users_info.items():
        s = f'{key}:{val}\n'
        r+=[s.encode()]
    with open(path, 'wb') as f:
        f.writelines(r)