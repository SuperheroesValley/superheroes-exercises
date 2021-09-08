class Solution:
    def trap(self, height):
        stack = [(0, height[0])]
        capacity = 0
        
        for i in range(1, len(height)):
            if not stack or height[i] < stack[-1][1]: #descending
                stack.append((i, height[i]))
                
            else:
                # il primo elemento dello stack e' sempre a distanza 1
                lastHeight = -1
                while stack:
                    h = min(stack[-1][1], height[i]) - lastHeight
                    w = i - stack[-1][0] - 1
                    print(f"calcolo rettangolo {h}x{w} per roccia ({i}, {height[i]}) e stack ({stack[-1][0]}, {stack[-1][1]})")
                    capacity += h * w
                    lastHeight = stack[-1][1]
                    if height[i] < stack[-1][1]:
                        break
                    stack.pop()
                stack.append((i, height[i]))
            
        return capacity
