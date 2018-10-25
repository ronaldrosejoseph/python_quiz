# Overlap exists only between the max of the starting points and min of ending points of two lines
# So for overlaps if we subtract min of ending points and max of the starting points of the two lines we would get
# positive values else no overlap
def lines_overlap(a, b):
    if (min(a[1], b[1]) - max(a[0], b[0])) > 0:
        return True
    return False

# Let a and b be the two lines
a = (4, 9)
b = (2, 6)

print(lines_overlap(a,b))
