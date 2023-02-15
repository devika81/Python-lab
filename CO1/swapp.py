def chars_mix_up(a,b):
    new_a=a[0]+b[1]+a[2:]
    new_b=b[0]+a[1]+b[2:]
    return new_a+''+new_b
print(chars_mix_up('nice','cake'))
