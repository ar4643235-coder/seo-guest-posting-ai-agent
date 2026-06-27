def generate_keywords(niche):
    keywords = [
        f"{niche} tips",
        f"best {niche} tools",
        f"{niche} guide for beginners",
        f"how to improve {niche}"
    ]
    return keywords

def generate_content_brief(keyword):
    brief = f"""
    Content Brief for: {keyword}
    - Target audience: SEO professionals & marketers
    - Goal: Rank for '{keyword}'
    - Suggested structure: Intro, Benefits, Steps, Conclusion
    - Word count: 1200-1500 words
    """
    return brief

def generate_outreach_email(website_name, niche):
    email = f"""
    Subject: Guest Post Collaboration for {website_name}

    Hi Team,

    I came across {website_name} and really enjoyed your content on {niche}.
    I'd love to contribute a high-quality guest post that adds value to your readers.

    Looking forward to collaborating!

    Best regards,
    SEO Outreach Agent
    """
    return email

niche = "guest posting"
keywords = generate_keywords(niche)
print("Generated Keywords:", keywords)

for k in keywords:
    print(generate_content_brief(k))

print(generate_outreach_email("TechBlog.com", "guest posting"))
