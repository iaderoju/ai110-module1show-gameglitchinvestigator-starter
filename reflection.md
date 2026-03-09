# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? 

It looked solid just like a simple kiddie game website. I noticed there were simple buttons to press that were straight forward on navigating the game.

- List at least two concrete bugs you noticed at the start  

 1. The game requires you to press New game when restarting, but once you do that it doesn't allow you to submit more guesses on the second attempt.

 2. I also notice the correct answers are not correlated to the hints.

 3.Range is also not correct, some numbers are in the negative and some are over the range. 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 

Claude

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

I gave claude context on the broken new game button and it told me that the "status" in the st.session_state.attemps is the culprit. st.stop() tells Streamlit to halt the page right there — so the text input box and Submit button never appear. That's the freeze.  The fix is to also add st.session_state.status = "playing" inside the New Game block so the game knows it's back to an active state. Refer:Lines 135-144

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

The ranges were still in the negatives even after making that known to the AI. check_guess was suggested to tweak.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
 
  I ran a manual fix on the new  game button and it worked. Flawless and consistent test on that fix.

- Did AI help you design or understand any tests? How?

It helped very well with how the code is supposed to be built. For example,  I asked the bot to implement the correct hints to supply a better message for the guesses. Added correct direction.
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
The secret number changes to retain the mystery behind the game.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would say that streamlit is your favorite teacher that checks your final draft of your project and offers constructive feedback.

- What change did you make that finally gave the game a stable secret number?
Working on the secret guess' returns.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  
  The agent mode is definitely fast and efficient. Definitely will be extra cautious with implementing the final product.

- What is one thing you would do differently next time you work with AI on a coding task?

I'd like to try to build the whole code with the AI on my next task and see how good it is at preparing the code in comparison to me on my own.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

In simple terms, there are getting better. AI code is advancing.

Breakout room 17