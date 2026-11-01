# Five practical exercises
1. Run all three sample interactions. Compare each complete output to sample_data/examples.json. Success: exact demo matches.
2. Submit whitespace and an 81-character name through greet. Success: both raise ValueError, without provider calls.
3. Add a fourth tone and a parameterized assertion for its closing sentence. Success: UI and function agree.
4. Inject a RunnableLambda returning AIMessage. Inspect the prompt messages. Success: all three variables reach the mock and the output is plain text.
5. Switch to live mode with no key. Success: an actionable error and no stale success canvas. Explain why mocking this path cannot prove provider authentication.
