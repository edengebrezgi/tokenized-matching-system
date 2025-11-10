import hashlib

def tokenize_email(email: str) -> str:
    """
    Convert a real email into a tokenized version that cannot be reversed.
    """
    if not isinstance(email, str):
        return None
    return hashlib.sha256(email.lower().encode()).hexdigest()

if __name__ == "__main__":
    sample = "example@email.com"
    print("Original:", sample)
    print("Tokenized:", tokenize_email(sample))
