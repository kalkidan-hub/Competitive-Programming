def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = abs(ax2-ax1) * abs(ay2-ay1)
        area2 = abs(bx2-bx1) * abs(by2-by1)
        # check intersection
        conditionX = (bx1 <= ax2 and bx2 >= ax1) or (bx2 <= ax2 and bx1 >= ax1)
        conditionY = (by1 <= ay2 and by2 >= ay1) or (by2 <= ay2 and by1 >= ay1)
        
        if conditionX and conditionY:
            intersectArea = abs(min(ax2,bx2)-max(bx1,ax1)) * abs(min(ay2,by2)-max(by1,ay1))
            print(area2 == intersectArea or area1 == intersectArea)
        else: 
            intersectArea = 0
        return area1 + area2 - intersectArea
        

# print(computeArea(0,0,0,0,-1,-1,1,1))