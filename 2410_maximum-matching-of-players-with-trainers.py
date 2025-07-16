class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        """
        greedy, two pointers, sort

        intuition: to fully utilize each trainer, you want to match them with player with largest
        ability that they can accommodate

        time: O(nlogn + mlogm + n)
        space: O(1)
        """
        count = 0

        players.sort(reverse=True)
        trainers.sort(reverse=True)

        n = len(players)
        m = len(trainers)

        i = j = 0
        while i < n and j < m:
            capacity = trainers[j]
            ability = players[i]
            if ability <= capacity:
                count += 1
                j += 1
            i += 1
        
        return count

