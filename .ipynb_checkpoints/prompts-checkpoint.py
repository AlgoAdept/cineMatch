def build_prompt(user_input):
    return f"""
You are an expert in matching people to fictional characters from movies and shows.

Based on the personality description below, suggest the ONE most similar fictional character.
Give:
- Character name
- Show/movie
- 2–3 sentence reason why they match
- A quote from the character

Personality: {user_input}
"""
