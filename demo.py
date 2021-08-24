
print("Mời bạn nhập vào một số nguyên:")
a = int(input())
b: int = int(a/3600)
c: int = int((a-b*3600)/60)
d: int = int(a-b*3600-c*60)
print(b, "giờ,", c, 'phút,', d, 'giây')

