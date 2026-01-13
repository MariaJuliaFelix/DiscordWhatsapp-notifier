KEYWORDS = ["reunião", "prazo", "urgente"]

def should_notify(message_content):
    content = message_content.lower()
    return any(keyword in content for keyword in KEYWORDS)
