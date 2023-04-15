from helpers import big_entry 

def return_lwh(array):
    l, w, h = int(array[0]), int(array[1]), int(array[2])
    return l,w,h

def calculate_suface(array):
    l, w, h = return_lwh(array)
    extra = min(l*w,w*h,h*l)
    return (2*l*w) + (2*w*h) + (2*h*l) + extra

def split_entry_by_x(entry):
    return entry.split("x")
     
def split_big_entry_by_n(big_entry):
    return big_entry.split("\n")

def calculate_dimensions_for_ruban(array):
    l, w, h = return_lwh(array)
    bow = l*w*h
    ribbon = 2 *  min( l + w, w + h, h + l)
    feet = bow + ribbon
    return feet

if __name__ == "__main__":
    sum = 0
    entry = split_big_entry_by_n(big_entry)
    for elt in entry:
        sum += calculate_dimensions_for_ruban(split_entry_by_x(elt)) 
    print(sum) #3842356

