#!/usr/bin/env python3
"""
Simple Number Puzzle Game - Under 100 lines!
Uses arithmetic (+ - * / %), comparison (== != > < >= <=), 
logical (and or not), and conditional (if elif else) operators
"""

import random

def arithmetic_puzzle():
    """Arithmetic puzzles using +, -, *, /, % operators"""
    a, b, c = random.randint(1, 20), random.randint(1, 20), random.randint(1, 10)
    puzzles = [(f"What is {a} + {b}?", a + b), (f"What is {a} - {b}?", a - b), 
              (f"What is {a} * {c}?", a * c), (f"What is {a} % {c}?", a % c),
              (f"What is ({a} + {b}) * {c}?", (a + b) * c)]
    question, answer = random.choice(puzzles)
    print(f"🔢 {question}")
    try:
        return int(input("Answer: ")) == answer
    except ValueError:
        return False

def comparison_puzzle():
    """Comparison puzzles using ==, !=, >, <, >=, <= operators"""
    a, b, c = random.randint(1, 50), random.randint(1, 50), random.randint(1, 20)
    puzzles = [(f"Is {a} == {b}?", a == b), (f"Is {a} != {b}?", a != b),
              (f"Is {a} > {b}?", a > b), (f"Is {a} < {b}?", a < b),
              (f"Is ({a} + {b}) > ({c} * 3)?", (a + b) > (c * 3))]
    question, answer = random.choice(puzzles)
    print(f"⚖️ {question}")
    user_input = input("Answer (True/False): ").lower()
    user_answer = user_input in ['true', 't', 'yes', 'y']
    return user_answer == answer

def logical_puzzle():
    """Logical puzzles using and, or, not operators"""
    p, q = random.choice([True, False]), random.choice([True, False])
    puzzles = [(f"If p={p}, q={q}, what is p and q?", p and q),
              (f"If p={p}, q={q}, what is p or q?", p or q),
              (f"If p={p}, what is not p?", not p),
              (f"If p={p}, q={q}, what is (p and q) or (not p)?", (p and q) or (not p))]
    question, answer = random.choice(puzzles)
    print(f"🧠 {question}")
    user_input = input("Answer (True/False): ").lower()
    user_answer = user_input in ['true', 't', 'yes', 'y']
    return user_answer == answer

def conditional_puzzle():
    """Conditional puzzles using if, elif, else statements"""
    x = random.randint(1, 100)
    if x > 50:
        answer = "high"
    elif x > 25:
        answer = "medium"
    else:
        answer = "low"
    
    print(f"🔀 Given x = {x}, what will this code output?")
    print("if x > 50: result = 'high'")
    print("elif x > 25: result = 'medium'")
    print("else: result = 'low'")
    
    user_answer = input("Answer: ").strip().lower()
    return user_answer == answer.lower()

def sequence_puzzle():
    """Number sequence puzzles using arithmetic patterns"""
    start = random.randint(1, 10)
    puzzles = [(f"Complete: {start}, {start+2}, {start+4}, ?", start + 6),
              (f"Complete: {start}, {start*2}, {start*4}, ?", start * 8),
              (f"Complete: {start}, {start**2}, {start**3}, ?", start ** 4)]
    question, answer = random.choice(puzzles)
    print(f"🔢 {question}")
    try:
        return int(input("Answer: ")) == answer
    except ValueError:
        return False

def play_game():
    """Main game loop - simplified version"""
    print("🧮 SIMPLE NUMBER PUZZLE GAME 🧮")
    print("=" * 40)
    print("Solve puzzles using different operators!")
    print("Arithmetic: + - * / %")
    print("Comparison: == != > < >= <=")
    print("Logical: and or not")
    print("Conditionals: if elif else")
    print("=" * 40)
    
    score = 0
    puzzles = [arithmetic_puzzle, comparison_puzzle, logical_puzzle, conditional_puzzle, sequence_puzzle]
    
    for round_num in range(1, 6):  # 5 rounds
        print(f"\n🎯 ROUND {round_num}")
        print("-" * 20)
        
        # Pick 2 random puzzles per round
        round_puzzles = random.sample(puzzles, 2)
        round_score = 0
        
        for puzzle_func in round_puzzles:
            if puzzle_func():
                print("✅ Correct!")
                round_score += 1
                score += 10
            else:
                print("❌ Wrong!")
        
        print(f"Round {round_num} Score: {round_score}/2")
    
    print(f"\n🏆 FINAL SCORE: {score}/100")
    if score >= 60:
        print("🎉 Great job! You mastered the operators!")
    else:
        print("💪 Keep practicing! Try again!")

if __name__ == "__main__":
    play_game()