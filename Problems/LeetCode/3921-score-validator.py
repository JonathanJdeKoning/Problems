class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0

        for event in events:
            if event.isdigit():
                score += int(event)
                continue
            if event == "WD" or event == "NB":
                score += 1
                continue
            counter += 1
            if counter == 10: break

        return [score, counter]
