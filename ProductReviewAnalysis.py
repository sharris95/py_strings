# Task 1: Keyword Highlighter
def highlight_keywords(reviews, keywords):
    highlighted_reviews = []
    for review in reviews:
        for keyword in keywords:
            review = review.replace(keyword, keyword.upper())
        highlighted_reviews.append(review)
    return highlighted_reviews

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]

keywords = ["good", "excellent", "bad", "poor", "average"]

highlighted_reviews = highlight_keywords(reviews, keywords)
for review in highlighted_reviews:
    print(review)

# Task 2: Sentiment Tally
def sentiment_tally(reviews, positive_words, negative_words):
    positive_count = 0
    negative_count = 0
    for review in reviews:
        words = review.split()
        for word in words:
            if word.lower() in positive_words:
                positive_count += 1
            elif word.lower() in negative_words:
                negative_count += 1
    return positive_count, negative_count

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

positive_count, negative_count = sentiment_tally(reviews, positive_words, negative_words)
print(f"Positive words: {positive_count}, Negative words: {negative_count}")

# Task 3: Review Summary
def summarize_review(review):
    if len(review) <= 30:
        return review
    end_index = 30
    while end_index > 0 and review[end_index] != ' ':
        end_index -= 1
    if end_index == 0:
        return review[:30] + "…"
    return review[:end_index] + "…"

summaries = [summarize_review(review) for review in reviews]
for summary in summaries:
    print(summary)