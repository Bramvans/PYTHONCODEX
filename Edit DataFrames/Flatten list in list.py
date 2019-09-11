# =============================================================================
# Flatten list and extract data
# =============================================================================
# example of lists in a list
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]


def flatten(input_list):
    output_list = []
    for element in input_list:
        if type(element) == list:
            output_list.extend(flatten(element))
        else:
            output_list.append(element)
    return output_list

a = flatten(lst)

# flatten turns it into a single slicable list [1, 2, 3, 4, 5, 6, 7, 8]

a[7:8]

#output would be the "Hello"