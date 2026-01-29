def largestRectangleArea(heights) -> int:
    max_area = 0
    stack = [-1]
    heights.append(0)

    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            bar = stack.pop()
            area = heights[bar] * (i-stack[-1]-1)
            max_area = max(area, max_area)
        
        stack.append(i)


    return max_area

largestRectangleArea([7,1,7,2,2,4])
        