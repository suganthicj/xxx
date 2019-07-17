
# Function to check if a given string is a vowel 
def vowel(c): 
      
    # creating a list of vowels 
    v = list("aeiou") 
      
    # if the character is a vowel return True 
    if c in v: return True
    return False
  
# Function to check if a vowel 
# string is palindrome 
def palindrome(s): 
      
    # create a empty list 
    v = [] 
      
    # append all vowels into the list 
    for i in s: 
        if vowel(i):v.append(i) 
      
    # if the length of the vowel 
    # string is 0 then print -1 
    if len(v)== 0: print("-1") 
      
    # else check if it is a palindrome 
    else: 
        # create a reversed string 
        x = v[::-1] 
          
        # initialize a flag 
        f = 1
        for i in range(len(x)): 
              
            # if the characters are not the same  
            if x[i]!= v[i]: 
                  
                # set the flag to 0 
                f = 0
                break
                  
        if f == 1: print("YES") 
        else: print("NO") 
          
# Driver Code 
s = 'abcuhuvmnba'
  
# calling the main function 
palindrome(s.strip()) 
