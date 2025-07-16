def segment_length(Ap, Ak, Bp, Bk):
    #asked chatgpt what the formula should be

    #preconditions:
    
    start_intersection = max(Ap,Bp)
    end_intersection = min(Ak,Bk)

    if start_intersection <= end_intersection:
        segment = (start_intersection,end_intersection)
        print(segment)
    else:
        print("None")
