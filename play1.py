import json

v_str = '{"id":100, "name":"홍길동"}'
v_user = json.loads(v_str)

print(f"User Name is {v_user['name']}")


def userInfo(_user):
  fv_id = _user["id"]
  fv_name = _user["name"]
  return f'User Id is {fv_id}, User Name is {fv_name}'


print(userInfo(v_user))
