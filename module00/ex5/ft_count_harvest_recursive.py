def ft_helper(days):
    if days > 0:
        ft_helper(days - 1)
        print(f"Day {days}")

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    ft_helper(days)
    print("Harvest time!")

ft_count_harvest_recursive()