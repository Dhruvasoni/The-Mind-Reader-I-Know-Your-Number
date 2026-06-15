"""
╔══════════════════════════════════════════════════════════╗
║           🔮  THE MIND READER  🔮                        ║
║        "I can read your thoughts..."                     ║
║                                                          ║
║  Code in Place - Final Project                           ║
║  Concept: Mind Reading via Binary Elimination Magic      ║
╚══════════════════════════════════════════════════════════╝
"""

import time
import random
import sys

# ─── Utility: dramatic typing effect ───────────────────────────────────────────
def type_print(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def pause(seconds=1.0):
    time.sleep(seconds)

def loading(message="Analyzing", dots=5, delay=0.4):
    sys.stdout.write(message)
    sys.stdout.flush()
    for _ in range(dots):
        time.sleep(delay)
        sys.stdout.write(".")
        sys.stdout.flush()
    print()

# ─── Show a "magic card" of numbers ────────────────────────────────────────────
def show_card(card_num, numbers):
    cols = 8
    rows = [numbers[i:i+cols] for i in range(0, len(numbers), cols)]
    print(f"\n  ┌─────────────────────────────────────┐")
    print(f"  │           ✨  CARD {card_num}  ✨              │")
    print(f"  ├─────────────────────────────────────┤")
    for row in rows:
        row_str = "  ".join(f"{n:2}" for n in row)
        print(f"  │  {row_str:<37}│")
    print(f"  └─────────────────────────────────────┘")

# ─── Generate cards using binary (powers of 2) trick ──────────────────────────
def generate_cards():
    """
    Each card contains numbers whose binary representation has a specific bit set.
    Card 1 → bit 0 (value 1)
    Card 2 → bit 1 (value 2)
    Card 3 → bit 2 (value 4)
    Card 4 → bit 3 (value 8)
    Card 5 → bit 4 (value 16)

    The secret number = sum of the first number on each card the user says "yes" to.
    That first number is always the power of 2 for that card.
    """
    cards = []
    for bit in range(5):           # 5 cards → numbers 1-31
        power = 2 ** bit
        card_numbers = [n for n in range(1, 32) if n & power]
        cards.append((power, card_numbers))
    return cards

# ─── Dramatic reveal ────────────────────────────────────────────────────────────
def reveal(number):
    pause(0.5)
    type_print("\n  🌀 Connecting to your mind...", delay=0.04)
    loading("  📡 Scanning brainwaves", dots=6, delay=0.3)
    pause(0.5)

    # Fake "wrong" guesses for drama
    fake_guesses = [n for n in range(1, 32) if n != number]
    dramatic_wrongs = random.sample(fake_guesses, min(3, len(fake_guesses)))

    type_print("\n  🔍 Filtering possibilities...", delay=0.04)
    for g in dramatic_wrongs:
        print(f"     ✗  {g}  ... eliminated")
        time.sleep(0.25)

    pause(0.6)
    loading("  🧠 Locking on to your number", dots=5, delay=0.35)
    pause(0.8)

    print()
    print("  ╔══════════════════════════════════╗")
    type_print(f"  ║   🔮  YOUR NUMBER IS ...  {number:2}  !!  ║", delay=0.05)
    print("  ╚══════════════════════════════════╝")
    print()

# ─── Get a yes/no answer from user ─────────────────────────────────────────────
def ask_yes_no(prompt):
    while True:
        ans = input(prompt).strip().lower()
        if ans in ("y", "yes", "haan", "ha", "1"):
            return True
        elif ans in ("n", "no", "nahi", "nhi", "0"):
            return False
        else:
            print("  ⚠️  Please type  y  or  n")

# ─── Score / grade your result ──────────────────────────────────────────────────
def give_verdict(correct):
    if correct:
        verdicts = [
            "🧿 The Mind Reader NEVER fails!",
            "🌟 Pure magic. No other explanation.",
            "🔮 Your mind is an open book to me!",
            "🎩 Did you see that coming? I did. 😏",
        ]
        print("  " + random.choice(verdicts))
    else:
        print("  🤔 Hmm... the cosmic forces are disturbed today.")
        print("  (Tip: Answer every card honestly and watch the magic work!)")

# ─── Play one full round ────────────────────────────────────────────────────────
def play_round():
    print()
    type_print("  Think of ANY number between 1 and 31.", delay=0.04)
    type_print("  Don't say it out loud. Just hold it in your mind. 🧘", delay=0.04)
    pause(1.5)

    cards = generate_cards()
    secret = 0  # We'll build this from user's answers

    for i, (power, numbers) in enumerate(cards):
        show_card(i + 1, numbers)
        pause(0.3)
        is_there = ask_yes_no(f"\n  Is your number on Card {i+1}? (y/n): ")
        if is_there:
            secret += power
        print()

    if secret == 0:
        type_print("\n  🤔 Hmm... it seems you said No to everything.", delay=0.04)
        type_print("  Did you pick 0? That's not between 1-31, cheater! 😄", delay=0.04)
        return

    reveal(secret)

    correct = ask_yes_no("  Was I right? (y/n): ")
    give_verdict(correct)

# ─── Stats tracker ──────────────────────────────────────────────────────────────
def show_stats(wins, total):
    print(f"\n  📊  Session Stats: {wins}/{total} correct guesses", end="")
    if total > 0:
        pct = int((wins / total) * 100)
        bar = "█" * (pct // 10) + "░" * (10 - pct // 10)
        print(f"  [{bar}] {pct}%")
    else:
        print()

# ─── Main ───────────────────────────────────────────────────────────────────────
def main():
    print()
    print("  ╔══════════════════════════════════════════════════╗")
    print("  ║       🔮   W E L C O M E   T O   T H E        ║")
    print("  ║            M I N D   R E A D E R               ║")
    print("  ║                                                  ║")
    print("  ║   I will read your mind using ancient           ║")
    print("  ║   mathematics and cosmic energy. 🌌             ║")
    print("  ╚══════════════════════════════════════════════════╝")
    print()
    type_print("  How does it work?", delay=0.05)
    type_print("  You think of a number (1–31). I show you 5 magic cards.", delay=0.03)
    type_print("  You just tell me YES or NO for each card.", delay=0.03)
    type_print("  I will reveal your number. Every. Single. Time. 🔮\n", delay=0.03)
    pause(1)

    wins = 0
    total = 0

    while True:
        input("  ── Press ENTER to begin ──")
        play_round()

        total += 1
        again = ask_yes_no("\n  Was I correct? Count it in stats? (y/n): ")
        if again:
            wins += 1

        show_stats(wins, total)
        print()

        play_again = ask_yes_no("  Try again? (y/n): ")
        if not play_again:
            break

    print()
    type_print("  🙏 Thanks for playing The Mind Reader!", delay=0.04)
    type_print("  Remember: magic is just math in disguise. 🔮✨", delay=0.04)
    show_stats(wins, total)
    print()

if __name__ == "__main__":
    main()
