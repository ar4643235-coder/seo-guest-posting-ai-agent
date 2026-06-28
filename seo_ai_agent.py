"""
SEO Guest Posting AI Agent
Decentralize AI Hackathon — Nosana Decentralized Compute Track

This agent automates:
1. Keyword research
2. Content brief generation
3. Outreach email generation
4. Real AI-powered content suggestions (runs on Nosana GPU inference)
"""

from transformers import pipeline

# ----------------------------
# Static / Template Functions
# ----------------------------

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


# ----------------------------
# Real AI-Powered Function
# Runs inference on Nosana decentralized GPU network
# ----------------------------

def ai_generate_content_idea(keyword, generator):
    """
    Uses a real Hugging Face text-generation model
    (executed on Nosana GPU compute) to generate
    a short SEO tip for the given keyword.
    """
    prompt = f"Write a short, helpful tip about {keyword}:"
    result = generator(
        prompt,
        max_new_tokens=50,
        do_sample=True,
        temperature=0.8,
        repetition_penalty=1.5
    )
    return result[0]['generated_text']


# ----------------------------
# Demo / Test Run
# ----------------------------

if __name__ == "__main__":
    niche = "guest posting"
    keywords = generate_keywords(niche)
    print("Generated Keywords:", keywords)

    for k in keywords:
        print(generate_content_brief(k))

    print(generate_outreach_email("TechBlog.com", niche))

    # Real AI inference example (requires GPU + transformers)
    # generator = pipeline("text-generation", model="distilgpt2", device=0)
    # for k in keywords:
    #     print(f"\nKeyword: {k}")
    #     print(ai_generate_content_idea(k, generator))
