def build_prompt(description):
    return f"""
You are an expert Instagram caption writer.

Generate 5 short, catchy Instagram captions.

Rules:
- Each caption must be under 12 words
- Include emojis
- Include 2-3 hashtags
- Make them trendy and engaging

Image: {description}

Return only captions as a numbered list.
"""