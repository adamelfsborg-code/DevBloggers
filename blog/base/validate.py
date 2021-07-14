def password_check(passwd):
      
    SpecialSym =['$', '@', '#', '%']

    pwd_check = {
        'is_valid': True,
        'arg': ''
    }
      
    if len(passwd) < 6:
        pwd_check['is_valid'] = False
        pwd_check['arg'] = 'Password length should be at least 6'

        return pwd_check
          
    if len(passwd) > 20:
        pwd_check['is_valid'] = False
        pwd_check['arg'] = 'Password length should not be greater than 20'
          
        return pwd_check

    if not any(char.isdigit() for char in passwd):
        pwd_check['is_valid'] = False
        pwd_check['arg'] = 'Password should have at least one numeral'

        return pwd_check

    if not any(char.isupper() for char in passwd):
        pwd_check['is_valid'] = False
        pwd_check['arg'] = 'Password should have at least one uppercase letter'
        
        return pwd_check

    if not any(char.islower() for char in passwd):
        pwd_check['is_valid'] = False
        pwd_check['arg'] = 'Password should have at least one lowercase letter'
        
        return pwd_check

    if not any(char in SpecialSym for char in passwd):
        pwd_check['is_valid'] = False
        pwd_check['arg'] = 'Password should have at least one of the symbols $@#'

        return pwd_check
    
    return pwd_check
