def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    l, r = 0, len(height)-1
    area = 0
    while (l<r):
        h = min(height[l],height[r])
        area = max(area, h*(r-l))
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
    
    return area
    