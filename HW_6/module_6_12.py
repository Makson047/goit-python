import base64


def encode_data_to_base64(data):
    r=[]
    for el in data:
      pas_bytes = el.encode("utf-8")
      base64_bytes_pas = base64.b64encode(pas_bytes)
      base64_pas = base64_bytes_pas.decode("utf-8")
      r += [base64_pas]
    return r