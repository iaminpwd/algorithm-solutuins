#https://school.programmers.co.kr/learn/courses/30/lessons/1845

# 폰켓몬 리스트에서 선택할 수 있는 최대 수는 전체 개수의 절반이다.
# 리스트를 set으로 변환해 종류 수를 구한 뒤,
# 종류 수가 최대 선택 수보다 크거나 같으면 최대 선택 수를, 작으면 종류 수를 반환한다.

def solution(nums):
    answer=len(nums)//2
    nums=set(nums)

    if len(nums) >= answer:
        return answer
    return len(nums)
