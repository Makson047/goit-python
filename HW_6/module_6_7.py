def sanitize_file(source, output):
    b=''
    with open(source,'r') as f:
      a = f.read()
      for el in a:
        print(el)
        if el not in ['0','1','2','3','4','5','6','7','8','9']:
          b += el
    with open(output,'w') as fw:
      fw.write(b)