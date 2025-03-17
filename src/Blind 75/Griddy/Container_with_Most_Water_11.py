def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    l, r = 0, 0
    area = 0
    for i in range(1, len(height)):
        if height[i] > height[r]:
            r = i
            area = (r-l)*min(height[r], height[l])
        elif height[i] > height[l]:
            l = r
            r = i
            area = (r-l)*min(height[r], height[l])

    print(area)
    return area


maxArea([1,8,6,2,5,4,8,3,7]) #49


        