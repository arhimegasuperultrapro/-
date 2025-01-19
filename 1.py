def val_comp(val:int):
    ls = ["компьютер", "компьютера", "компьютеров"]
    len_ = len(str(val))
    if len_ > 1 and str(val)[-2] == "1":
        return f"{val} компьютеров"
    elif len_ > 1 and str(val)[-2] != "1":
        if str(val)[-1] in "234": return f"{val} {ls[1]}"
        elif str(val)[-1] == "1": return f"{val} {ls[0]}"
        else: return f"{val} {ls[2]}"
    else:
        if str(val)[-1] in "234": return f"{val} {ls[1]}"
        elif str(val)[-1] == "1": return f"{val} {ls[0]}"
        else: return f"{val} {ls[2]}"

for i in range(31):
    print(val_comp(i))