"""
2512. Reward top k students

- Every pos word in feedback +3
- Every neg word in feedback -1
- n feedback reports, 0-indexed string array report
- student_id array, also 0-indexed of student IDs receiving report[i]
   - each student id unique

- return top k students after sorting decreasing order by points
- if more than one student have points, get one with lower ID

1. need to find out if report is pos or neg
2. assign report to student
3. sort first by points desc, then by id desc
return top k

- seems that any one neg word is sufficient for negative feedback
"""
from typing import List
from queue import PriorityQueue


def top_students(positive_feedback: List[str], negative_feedback: List[str], report: List[str],
                 student_id: List[int], k: int) -> List[int]:
    n = len(student_id)
    word_map = {word: 3 for word in positive_feedback} | {word: -1 for word in negative_feedback}
    scores = []

    for i in range(n):
        score = 0
        for token in report[i].split(' '):
            if token in word_map:
                score += word_map[token]
        scores.append((student_id[i], score))
        print(scores)

    scores.sort(key=(lambda x: (-x[1], x[0])))
    ans = []
    for j in range(k):
        ans.append(scores[j][0])
    return ans


def top_students_pq(positive_feedback: List[str], negative_feedback: List[str], report: List[str],
                   student_id: List[int], k: int) -> List[int]:
    n = len(student_id)
    scores = PriorityQueue()
    word_map = {word: 3 for word in positive_feedback} | {word: -1 for word in negative_feedback}

    for i in range(n):
        score = 0
        for token in report[i].split(' '):
            score += word_map.get(token, 0)
        scores.put((-score, student_id[i]))
        if scores.qsize() > k:
            scores.get()

    ans = []
    for j in range(k):
        ans.append(abs(scores.get()[1]))
    return ans


print(top_students_pq(positive_feedback=["smart", "brilliant", "studious"], negative_feedback=["not"],
                     report=["this student is studious", "the student is smart"], student_id=[1, 2], k=2))
