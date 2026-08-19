class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        people = []

  
        for i in range(len(names)):
            people.append([heights[i], names[i]])

        people.sort(reverse=True)

        answer = []

        for person in people:
            answer.append(person[1])

        return answer
        