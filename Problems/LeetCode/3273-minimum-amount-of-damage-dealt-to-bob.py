class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        def toKill(x):
            return ceil(x/power)
        ouch = 0
        murd = sum(damage)
        prio = [damage[x] / toKill(health[x]) for x in range(len(health))]

        enem = sorted(zip(prio, damage, health))
        while enem:
            currPrio, currDam, currHealth = enem.pop()
            time = toKill(currHealth)
            ouch += murd*time
            murd -= currDam

        return ouch