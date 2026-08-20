
import tiktoken

encoding = tiktoken.get_encoding("cl100k_base")


def show_tokens(text: str):
    token_ids = encoding.encode(text)
    tokens_as_text = [encoding.decode([t]) for t in token_ids]

    print(f"\nText: {text!r}")
    print(f"Characters: {len(text)}  |  Words: {len(text.split())}  |  Tokens: {len(token_ids)}")
    print("Token breakdown:", tokens_as_text)


if __name__ == "__main__":
    print("=" * 60)
    print("PART A: Common words vs rare/made-up words")
    print("=" * 60)
    show_tokens("Equatex builds trading signals")
    show_tokens("Equatex builds cryptozoological blockchainification")  # made-up word

    print("\n" + "=" * 60)
    print("PART B: Numbers and symbols tokenize weirdly")
    print("=" * 60)
    show_tokens("BTC is at $67,432.19 up 3.2% today")

    print("\n" + "=" * 60)
    print("PART C: Whitespace and casing matter")
    print("=" * 60)
    show_tokens("hello")
    show_tokens(" hello")   # leading space is often part of the token!
    show_tokens("Hello")    # different casing = different token

    print("\n" + "=" * 60)
    print("YOUR TURN — edit the lines below and re-run")
    print("=" * 60)
    # TODO 1: Paste a real tweet/social post from your Equatex scraping
    #         pipeline here and see how many tokens it costs.
    show_tokens("PASTE SOMETHING HERE")

    # TODO 2: Try a restaurant order sentence like a customer might say
    #         on a phone call, and count tokens.
    show_tokens("I'd like two chicken burgers and a large coke please")

    # CHALLENGE: Write a function `estimate_cost(text, price_per_1k_tokens)`
    # that tells you how much a given prompt would cost to send.
    def estimate_cost(text: str, price_per_1k_tokens: float) -> float:
        # YOUR CODE HERE
        pass