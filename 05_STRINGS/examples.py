name = "alice"
print(name.upper())        # ALICE
print(len(name))           # 5
print(name[0])             # a

email = "  Ravi@Gmail.COM  "
clean_email = email.strip().lower()
print(clean_email)         # ravi@gmail.com
print("@" in clean_email)  # True — valid email check!

text = "abcdefghij"

print(text[2:8:2])    # ceg  — start=2, stop=8, step=2
print(text[::-2])     # jhfd — reversed, every 2nd char
print(text[7:2:-1])   # hgfed — from index 7 down to 3