def reverse_sentence(sentence: str) -> str:
    try:
        if not isinstance(sentence, str):
            raise TypeError(f"Input must be a string, got {type(sentence).__name__}")
        
        if not sentence.strip():
            raise ValueError("Sentence cannot be empty or only whitespace")
        
        words = sentence.strip().split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)
        
    except Exception as e:
        raise Exception(f"Error in reverse_sentence: {e}")

def get_grade(mark: int) -> str:
    try:
        if not isinstance(mark, int):
            raise TypeError(f"Mark must be an integer, got {type(mark).__name__}")
        
        if not (0 <= mark <= 100):
            raise ValueError(f"Mark must be between 0 and 100, got {mark}")
        
        if mark >= 80:
            return 'A'
        elif mark >= 65:
            return 'B'
        elif mark >= 50:
            return 'C'
        elif mark >= 40:
            return 'D'
        else:
            return 'F'
            
    except Exception as e:
        raise Exception(f"Error in get_grade: {e}") from e

def count_words(text: str) -> int:
    try:
        if not isinstance(text, str):
            raise TypeError(f"Input must be a string, got {type(text).__name__}")
        
        if not text.strip():
            return 0
        
        return len(text.strip().split())
        
    except Exception as e:
        raise Exception(f"Error in count_words: {e}")

def capitalize_words(text: str) -> str:
    try:
        if not isinstance(text, str):
            raise TypeError(f"Input must be a string, got {type(text).__name__}")
        
        if not text.strip():
            return text
        
        return ' '.join(word.capitalize() for word in text.split())
        
    except Exception as e:
        raise Exception(f"Error in capitalize_words: {e}")

def count_vowels_consonants(text: str) -> tuple[int, int]:
    try:
        if not isinstance(text, str):
            raise TypeError(f"Input must be a string, got {type(text).__name__}")
        
        vowels = "aeiouAEIOU"
        vowel_count = 0
        consonant_count = 0
        
        for char in text:
            if char.isalpha():
                if char in vowels:
                    vowel_count += 1
                else:
                    consonant_count += 1
        
        return vowel_count, consonant_count
        
    except Exception as e:
        raise Exception(f"Error in count_vowels_consonants: {e}")
