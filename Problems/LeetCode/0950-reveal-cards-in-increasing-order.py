class Solution:
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        deck.sort()
        st = deque()
        st.append(deck[n - 1])
        for i in range(n - 2, -1, -1):
            st.appendleft(st.pop())
            st.appendleft(deck[i])
        revealed = []
        while st:
            revealed.append(st.popleft())
        return revealed