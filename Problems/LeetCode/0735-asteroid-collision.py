class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        ans = []
        for asteroid in asteroids:
            backward = asteroid < 0
            if not stack:
                if not backward:
                    stack.append(asteroid)
                else:
                    ans.append(asteroid)
                continue


            if backward:
                while stack[-1] > 0 and abs(stack[-1]) <= abs(asteroid):
                    forw = stack.pop()
                    if abs(forw) == abs(asteroid): break
                    if not stack:
                        ans.append(asteroid)
                        break
            else:
                stack.append(asteroid)
        return ans + stack