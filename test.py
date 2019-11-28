def insert_intervals(intervals, new_interval):
    intervals.append(new_interval)
    
    intervals.sort(key=lambda x: x[0])
    
    inserted =[]
    
    for interval in intervals:
        if not inserted or inserted[-1][1] < interval[0]:
            inserted.append(interval)
        else:
            inserted[-1][1] = max(interval[1], inserted[-1][1])
            
    return inserted

intervals=[[1,2], [3,5], [6, 7], [8, 10], [12, 16]]
new = [4,8]
print(insert_intervals(intervals, new))