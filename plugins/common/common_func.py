def get_sftp():
    print('SFTP 작업을 시작합니다.')

def regist(name, sex, *args):
    print(f'성명 : {name}')
    print(f'성별 : {sex}')
    print(f'기타 : {args}')

def regist2(name, sex, *args, **kwargs):
    print(f'성명 : {name}')
    print(f'성별 : {sex}')
    print(f'기타 : {args}')
    email=kwargs['email'] or None
    phone=kwargs['phone'] or None
    if email:
	    print(email)
    if phone:
	    print(phone)
