# Five practical exercises

1. Run all sample contracts for Follow a thread over time; explain each expected field in your own words. Success: exact expected-field matches.
2. Explain why “Run-level versus thread-level analysis” matters. Change an input to demonstrate its effect. Success: record before/after evidence.
3. Submit an empty value and malformed JSON where applicable. Success: actionable input failure without a stale result.
4. Add one boundary case and one failure case to tests before extending the pipeline. Success: tests fail for the old behavior and pass for the intended change.
5. Replace an external dependency with an injected fake where applicable; otherwise inspect the deterministic stage. Success: explain what is tested and which live behavior remains unverified.
