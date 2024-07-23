def do_rectangles_overlap(L1, R1, L2, R2):
    L1x, L1y = L1
    R1x, R1y = R1
    L2x, L2y = L2
    R2x, R2y = R2
    
    # If one rectangle is to the left of the other
    if R1x < L2x or R2x < L1x:
        return False
    
    # If one rectangle is above the other
    if R1y > L2y or R2y > L1y:
        return False
    
    return True

# Example usage
L1 = (0, 10)  # Top-left corner of first rectangle
R1 = (10, 0)  # Bottom-right corner of first rectangle
L2 = (5, 5)   # Top-left corner of second rectangle
R2 = (15, 0)  # Bottom-right corner of second rectangle

if do_rectangles_overlap(L1, R1, L2, R2):
    print("Rectangles overlap.")
else:
    print("Rectangles do not overlap.")
