# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

Ans1:- 
- The game show hint function was not correct, feels like it randomly generated the hint as even if I guessed a number higher than the secret number it still kept showing the hint as go higher. 
- The game doesn't switch between the difficulty levels. I expected it to switch the range and number of tries based on the difficulty level. 
- The new game button doesn't reset the game. I expected it to reset the game and start a new game. 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

Ans2:-
I primarily used Copilot Agent Mode with "Gemini 3 Flash" to help with the refactoring and debugging. One example of a correct suggestion was when I asked how to persist the secret number in Streamlit - the AI correctly identified that I needed to use `st.session_state`. An incorrect or misleading suggestion occurred when I refactored the logic functions to return tuples - the AI moved the code correctly but forgot to update the `pytest` file, which caused all my automated tests to fail until I fixed them manually.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

Ans3:-
I decided a bug was fixed by first verifying it manually in the running app and then confirming it with automated tests. I added a new `test_score_penalty` case in `pytest` to ensure that every wrong guess correctly deducted 2 points from the session score. The AI helped me understand how to structure the `pytest` assertions, especially when dealing with the tuple return values from the logic utilities.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

Ans4:-
The secret number kept changing in the original app because Streamlit reruns the entire script from top to bottom every time a user interacts with a widget. Without `st.session_state`, every click causes the `random.randint` line to execute again, generating a brand new secret. I would explain to a friend that Streamlit "reruns" are like refreshing a page, and `session_state` is like a memory that keeps your data safe while the page refreshes itself.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

Ans5:-
One habit I want to reuse is separating core logic from UI code. Moving functions like `check_guess` into `logic_utils.py` made it possible to write unit tests without having to run the whole web app, which saved a lot of time. Next time, I will be more careful to review the entire codebase after a major AI refactor to catch secondary breakages (like the tests failing). This project showed me that while AI can write code quickly, the human developer's role in verifying and connecting the pieces is critical.
