def save_applicant_data(source, output):
    r=[]
    for d in source:
        s=''
        for key, val in d.items():
          s = s + str(val) + ','
        r+=[s[:-1]+'\n']
    print(r)
    with open(output, 'w') as f:
       f.writelines(r)