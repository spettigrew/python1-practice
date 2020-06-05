#define(def) a doubling function that passes arguments by value
"""
JS: 
function double(x) {
    return ()
}
const double = (x) => {}

"""

def mult2(x): # x is passed by value. The value of the variable is copied.
    return x * 2

# define a doubling function for a list of variables passed by reference. 'l' is a pointer to some list in memory. Ex: some_nums[(list)] 
# Simple variables get passed by value (str, bool, integers). Complex get passed by referenece (dicts, tuples, lists, sets, class objects) Comples is if variable passes more that one value. 
def mult2_list(l):
    for i in range(len(l)):
        l[i] *= 2
    return l

y = mult2(12)
print(y)

some_nums = [1, 2, 3, 4]
print(some_nums)
mult2_list(some_nums)
print(some_nums)