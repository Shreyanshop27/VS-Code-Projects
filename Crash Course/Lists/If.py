username=[" Eren" , "Sasha " , "Mikasa" , "  erwin " , " Armin " , " Jean  "]
admin = ["eren" , "erwin"]
for name in username:
    name=name.lower()
    name=name.strip()
    if name in admin:
        print(f"{name}, wanna see report ?")
    else:
        print(f"{name} welcome")
    