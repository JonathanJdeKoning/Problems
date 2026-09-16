# Definition for a street.
# class Street:
#     def openDoor(self):
#         pass
#     def closeDoor(self):
#         pass
#     def isDoorOpen(self):
#         pass
#     def moveRight(self):
#         pass
#     def moveLeft(self):
#         pass
class Solution:
    def houseCount(self, street: Optional['Street'], k: int) -> int:
        for _ in range(k+3):
            if street.isDoorOpen():
                street.closeDoor()
            street.moveRight()
        street.openDoor()
        street.moveLeft()
        count = 1
        while not street.isDoorOpen():
            count += 1
            street.moveLeft()
        return count