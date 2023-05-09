class StringUtility: 
    def __init__(self, string):
        self.string = string
    
    def __str__(self):
        return self.string

    def vowels(self):
        count = 0
        for char in self.string:
            if char in "aeiouAEIOU":
                count = count + 1
        if count >= 5:
            return "many"
        elif count < 5: 
            return str(count)  

    def bothEnds(self):
        if len(self.string) > 2:
            curr_str = self.string[0] + self.string[1] +self.string[-2] + self.string[-1]
            return curr_str
        else: 
            return ""

    def fixStart(self):
        if len(self.string) <= 1:
            return self.string

        first_char = self.string[0]
        rep_string = first_char + self.string[1:].replace(first_char, '*')
        return rep_string

    def asciiSum(self):
        a_sum = 0
        for char in self.string:
            a_sum += ord(char)
        return a_sum

    def cipher(self):
        result = ""
        for char in self.string:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                new_position = (ord(char) - start + len(self.string)) % 26
                char= chr(start + new_position)
            result += char
            result = result.replace(self.string, char)
        return result

