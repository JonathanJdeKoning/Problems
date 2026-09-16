class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = defaultdict(int)
        for i in range(lowLimit, highLimit+1):
            boxes[sum([int(x) for x in str(i)])]+=1
        return max([v for k,v in boxes.items()])