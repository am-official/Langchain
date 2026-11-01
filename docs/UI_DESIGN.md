# Interface standard
Every instructional app and capstone must have a polished graphical interface. Use a consistent midnight, violet, and mint palette, strong typographic hierarchy, generous spacing, restrained gradients, and readable cards. Streamlit native widgets retain keyboard support and labels. Avoid internal DOM class selectors and external font dependencies.

Always provide a useful example, explicit demo/live status, actionable empty and error states, visible success criteria, and responsive controls. Never imply demo output is model output. Hide secrets; never display raw provider exceptions. Render user/model text through native text widgets, not HTML interpolation. Each app remains self-contained: copy its small style function rather than importing another project.

Validate desktop and narrow layouts, contrast, keyboard focus, loading feedback, and long outputs before calling visual review complete. Automated functional UI tests do not establish visual approval.
