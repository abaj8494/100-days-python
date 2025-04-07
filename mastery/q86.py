def check_str_is_num(s):
  return s.replace('.', '', 1).isdigit()
check_str_is_num("6s")
check_str_is_num("s")
check_str_is_num("7")
check_str_is_num("4.0")
