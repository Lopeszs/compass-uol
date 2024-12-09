def soma(string):
    nums = string.split(',')
    soma = 0 
    for i in range (len(nums)):
        soma += int(nums[i])
    return soma
    
string = '1,3,4,6,10,76'

print(soma(string))