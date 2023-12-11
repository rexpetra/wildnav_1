def get_size(lst):
    if isinstance(lst, list):
        # If it's a list, recurse to the next dimension
        sizes = [get_size(sublist) for sublist in lst]
        return sizes
    else:
        # If it's not a list, it's a leaf element, return 1
        return 1

# Example usage:

my_list = [
    [1, 2, 3],
    [4, 5, 6],
    [
        [7, 8],
        [9, 10]
    ],
    [1,2,3,4,5]
]

sizes = get_size(my_list)
print("Size along each dimension:", sizes)
