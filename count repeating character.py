def longestSubstring(s, k) :
 
    # Store the required answer
    ans = 0
 
    # Create a frequency map of the
    # characters of the string
    freq = [0]*26
 
    # Store the length of the string
    n = len(s)
 
    # Traverse the string, s
    for i in range(n) :
 
        # Increment the frequency of
        # the current character by 1
        freq[ord(s[i]) - ord('a')] += 1
 
    # Stores count of unique characters
    unique = 0
 
    # Find the number of unique
    # characters in string
    for i in range(26) :
        if (freq[i] != 0) :
            unique += 1
 
    # Iterate in range [1, unique]
    for curr_unique in range(1, unique + 1) :
 
        # Initialize frequency of all
        # characters as 0
        Freq = [0]*26
 
        # Stores the start and the
        # end of the window
        start, end = 0, 0
 
        # Stores the current number of
        # unique characters and characters
        # occurring atleast K times
        cnt, count_k = 0, 0
 
        while (end < n) :
            if (cnt <= curr_unique) :
                ind = ord(s[end]) - ord('a')
 
                # New unique character
                if (Freq[ind] == 0) :
                    cnt += 1
 
                Freq[ind] += 1
 
                # New character which
                # occurs atleast k times
                if (Freq[ind] == k) :
                    count_k += 1
 
                # Expand window by
                # incrementing end by 1
                end += 1
             
            else :
                ind = ord(s[start]) - ord('a')
 
                # Check if this character
                # is present atleast k times
                if (Freq[ind] == k) :
                    count_k -= 1
 
                Freq[ind] -= 1
 
                # Check if this character
                # is unique
                if (Freq[ind] == 0) :
                    cnt -= 1
 
                # Shrink the window by
                # incrementing start by 1
                start += 1
 
            # If there are curr_unique
            # characters and each character
            # is atleast k times
            if ((cnt == curr_unique) and (count_k == curr_unique)) :
 
                # Update the overall
                # maximum length
                ans = max(ans, end - start)
 
    # Print the answer
    print(ans)
S = "ababbc"
K = 2
longestSubstring(S, K)
 
7
