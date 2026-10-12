def email(s: str):
    if " " in s:
        return False
    if "@" not in s:
        return False
    at_index = s.index("@")
    if "." not in s[at_index:]:
        return False
    return True
print(email("test@example.com")) #введите email на проверку