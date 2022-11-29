from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    
    for privacy in privacies:
        data = privacy.split(' ')
        
        date = datetime.strptime(data[0], "%Y.%m.%d")
        type = data[1]
        
        term = [s for s in terms if type in s][0].split()[1]
        
        
        
    
    return answer

if __name__ == '__main__':
    today = '2022.05.19'
    terms = ['A 6', 'B 12', 'C 3']
    privacies = ['2021.05.02 A', '2021.07.01 B', '2022.02.19 C', '2022.02.20 C']
    
    result = solution(today, terms, privacies)