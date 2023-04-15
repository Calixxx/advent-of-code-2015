from helpers import big_entry 

def calculate_suface(array):
    l, w, h = int(array[0]), int(array[1]), int(array[2])
    extra = min(l*w,w*h,h*l)
    return (2*l*w) + (2*w*h) + (2*h*l) + extra

def split_entry_by_x(entry):
    return entry.split("x")
     
def split_big_entry_by_n(big_entry):
    return big_entry.split("\n")

if __name__ == "__main__":
    sum = 0
    entry = split_big_entry_by_n(big_entry)
    for elt in entry:
        sum += calculate_suface(split_entry_by_x(elt)) 
    print(sum)  #1606483

    