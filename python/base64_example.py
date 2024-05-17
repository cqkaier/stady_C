import base64

st = 'hello word'
ste = base64.b64encode(st.encode('utf-8'))
print(ste.decode('utf-8'))
