# Prompt-Driven AI Judge – Rock Paper Scissors Plus

## Overview
This project is a small experiment in building an **AI-based judge** for a Rock-Paper-Scissors-style game, where the model evaluates free-text user inputs and decides what happened in a round.

The goal of the assignment was not to build a full game system, but to show how **prompt design and instructions** can drive reasoning, validation, and explanation.

---

## Why This Approach
I deliberately kept the code minimal and pushed most of the logic into the prompt.

The idea was to treat the LLM as a *referee*:
- it interprets what the user tried to play
- checks the move against the rules
- explains why a move is valid, invalid, or unclear

This avoids hardcoded rule trees and makes the decision process easier to inspect and reason about.

---

## Architecture Overview
The system is structured around three clear steps:

1. **Intent Understanding**  
   The model interprets the user’s free-text input and decides what move (if any) the user intended.

2. **Rule Enforcement**  
   All game rules (valid moves, bomb usage, edge cases) are enforced through the prompt itself rather than application logic.

3. **Response Generation**  
   The model returns a structured JSON response describing the decision, the reasoning behind it, and what happens next.

Only minimal state is managed outside the model.

---

## Prompt Design
The prompt explicitly:
- lists all valid moves and constraints
- instructs the model to mark ambiguous intent as `UNCLEAR`
- enforces the one-time use rule for the bomb
- requires a fixed JSON output format

No win/loss logic is implemented in code; the model is responsible for judging each round.

---

## State Handling
To keep the system simple, only two pieces of state are tracked:
- the current round number
- whether the user has already used the bomb

This state is passed into the prompt each round so the model can apply constraints consistently.

---

## Edge Cases Considered
While designing the prompt, I specifically tested and accounted for:
- ambiguous inputs like “rock or paper”
- invalid moves such as “fire” or “water”
- metaphorical or playful language
- repeated bomb usage across rounds
- unclear intent caused by emojis or slang

In these cases, the move is marked as `UNCLEAR` or `INVALID`, and the turn is wasted as defined in the rules.

---

## Output Format
Each round produces a JSON response containing:
- round number
- original user input
- interpreted move
- move validity
- explanation of the decision
- round outcome
- bomb usage status
- a short message indicating the next step

This makes the judge’s reasoning easy to verify and debug.

---

## What I Chose Not to Do
To stay aligned with the assignment focus, I avoided:
- large if-else or rule-based engines
- regex-heavy intent parsing
- databases or UI layers
- over-engineering with multiple agents or tools

---

## Possible Improvements
With more time, this could be extended to include:
- confidence scores for intent interpretation
- match-level summaries across rounds
- support for multiple players
- better handling of emojis and multilingual inputs

---

## Closing Notes
This project is meant to demonstrate how **careful prompt design** can replace large amounts of traditional control logic, while still producing consistent and explainable decisions.
