def clean_text(x):
    if isinstance(x, str):
        return x.strip().lower()
    return x