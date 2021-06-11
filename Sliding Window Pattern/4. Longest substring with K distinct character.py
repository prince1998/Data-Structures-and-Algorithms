# Longest Substring with K Distinct Character - Sliding Window

def longest_substring_with_k_distinct_character(str,K):
    window_start = 0
    character_frequency = {}
    max_len = 0

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char not in character_frequency:
            character_frequency[right_char] = 0
        character_frequency[right_char] += 1

        while len(character_frequency) > K:
            left_char = str[window_start]
            character_frequency[left_char] -= 1
            if character_frequency[left_char] == 0:
                del character_frequency[left_char]
            window_start += 1
        
        max_len = max(max_len,window_end-window_start+1)

    return max_len

str = "cbbebi"
K = 3
max_len = longest_substring_with_k_distinct_character(str,K)
print(max_len)