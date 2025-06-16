# Question 16
def print_tent(size):
    """f"""
    if size == 1:
        print("*")
    else:
        max_items = size * 2 - 1
        for i in range(1, size+1):
            total_items = i * 2 - 1
            spaces = int((max_items - total_items) / 2)
            pspaces = spaces * " "
            if i> 1:
                dash = total_items - 2
                dashs = dash * "-"
                print(f"{pspaces}*{dashs}*{pspaces}")
            else:
                print(f"{pspaces}*{pspaces}")


print_tent(1)

print()


print_tent(4)
print()
print_tent(5)