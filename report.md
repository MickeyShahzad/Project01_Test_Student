# Project 1 Report: Intelligent Search Visualizer

> [!IMPORTANT]
> **AUTOGRADER COMPLIANCE INSTRUCTIONS:**
> This report is parsed automatically by the autograder. To ensure you receive full credit for your work:
> 1. **Do not modify** the section headers (`## ...`) or bold field keys (e.g., `**Name:**`, `**Selected Region:**`, `**Live Deployment URL:**`, etc.).
> 2. **Write your answers directly after** the colon `:` of each field, replacing the placeholder text completely (including the outer brackets `[` and `]`).
> 3. **Maintain the file structure**. Changing headers, bold titles, or deleting lines can cause the autograder to miss your responses and award 0 marks.

---

## Student Information 
- **Name:** Muhammad Abdullah Shahzad
- **UID (netID):** mshah269
- **UIN:** 668184261

---

## Section 1: Selected City Region
- **Selected Region:** Illinois, USA

---

## Section 2: Map Graph Configuration
- **Total Cities Configured:** 22
- **Total Connection Edges:** 35
- **Graph Fully Connected:** Yes

---

## Section 3: Local Verification & Search Algorithms
*Check the algorithms you successfully ran and verified on your local development server by placing an `x` in the brackets (e.g., `[x]`):*
- [x] Breadth-First Search (BFS)
- [x] Depth-First Search (DFS)
- [x] Uniform Cost Search (UCS)
- [x] Iterative Deepening Search (IDS)
- [x] Greedy Best-First Search (Greedy)
- [x] A* Search (A*)

---

## Section 4: Deployed and Presentation Information
- **Deployment Platform:** Render
- **Live Deployment URL:** https://project01-test-student-shz0.onrender.com/
- **Video Presentation Link:** https://www.youtube.com/watch?v=81Cb96dQupw

---

## Section 5: Discussion
- **Which search algorithm is best for this route finding problem?** 
    A* is a strong choice because it considers both the distance already traveled and an estimated distance to the destination. In this project, that can give an optimal route while exploring fewer nodes than UCS when the heuristic behaves appropriately.
- **Search Efficiency (Nodes expanded/time taken comparison):** 
    In our Chicago-to-Springfield test, Greedy expanded the fewest nodes (4), while IDS expanded the most (70). A* expanded 11 nodes and found the same 205.43-mile route cost as UCS, which expanded 22 nodes. This shows how heuristic information can reduce the amount of searching.
- **Link the idea of search algorithm to today Generative AI.** 
    Search algorithms explore possible choices to find a useful solution. Modern generative-AI systems can also use search-related techniques for tasks such as planning, retrieving information, and evaluating possible alternatives.

