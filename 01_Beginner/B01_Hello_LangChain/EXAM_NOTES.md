# Five original practice questions
These are original foundation questions, not actual exam questions. Official alignment is unverified. Domain: Building Agents (provisional).

1. What executes a runnable with input? A invoke; B print; C export; D freeze. **A**: invoke runs the pipeline. print displays objects; export and freeze are not execution APIs. Easy.
2. What does StrOutputParser return here? A database; B plain text; C embeddings; D tool permissions. **B**: it extracts text. The other choices concern unrelated storage, vectors, or security. Easy.
3. Which stage can be substituted in a test? A only the UI; B only .env; C the model runnable; D none. **C**: injectable runnables permit controlled outputs; changing UI or configuration alone does not isolate model behavior. Medium.
4. Where should an API key be configured? A committed source; B public sample data; C error message; D environment/.env ignored by Git. **D**: external configuration avoids committing credentials; all other choices disclose them. Easy.
5. Does a prompt-model-parser chain establish an autonomous agent? A always; B only if styled; C no, no tool/control loop is present; D only on Windows. **C**: UI and operating system do not create agency, and composition alone is insufficient. Medium.

Reference targets for later verification: https://docs.langchain.com/oss/python/langchain/models and https://docs.langchain.com/oss/python/langchain/agents . Score one point each; revisit EXPLANATION for any missed question. No exam score is guaranteed.
