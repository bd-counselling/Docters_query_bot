def should_activate(text: str) -> bool:
    text = text.lower()
    return "hi samaira" in text or "query" in text

def classify_query(text: str) -> str:
    text = text.lower()

    if any(word in text for word in ["tech", "payment", "piracy", "login", "logout", "session", "device", "pdf"]):
        return "tech"

    elif any(word in text for word in ["new plan", "extension plan", "renew", "pricing"]):
        return "sales"

    elif any(word in text for word in ["hi", "hello", "thanks", "thank you", "feedback", "appreciate"]):
        return "basic"

    return "unknown"