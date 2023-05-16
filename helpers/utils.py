
  
# generate 5 digit uuid numaric number
def unique_number(digit):
    import uuid
    return str(int(str(uuid.uuid4().int)[:digit]))