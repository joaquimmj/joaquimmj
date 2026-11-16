### Hi, I'm Joaquim

I build AI tools for finance, and I study how LLM agents get numbers wrong. Economics and computer science student in Paris.

I'm building [Aptence](https://aptence.app): financial modeling tests for finance recruiting, graded automatically. Before that, I built [QuantAcademy](https://quantacademy.app) on my own, a finance interview prep platform with 5k users.

**Projects**

- [deskstack](https://github.com/joaquimmj/deskstack): an AI deal team inside Claude. It builds the model, checks every number against the filings and flags what a human should review.
- [freeterminal](https://github.com/joaquimmj/freeterminal): free US and European financial data for Claude, with the source of every number. One URL to paste.
- [cellrush](https://github.com/joaquimmj/cellrush): Monkeytype for spreadsheets. Excel shortcuts against the clock, keyboard only.
- [gapscout](https://github.com/joaquimmj/gapscout): finds problems worth building from real complaints and real search demand.

**Contributions**

- [Firecrawl](https://github.com/firecrawl/firecrawl) (YC S22, 200k stars): the crawler billed links to uppercase files like `.JPG` as pages. [Fix](https://github.com/firecrawl/firecrawl/pull/5750) in review.
- [Univer](https://github.com/dream-num/univer) (24k stars): I tested 500+ of its Excel functions against LibreOffice and found a formula engine crash and wrong results in SORT, SEARCH and ROUND. [Four fixes](https://github.com/dream-num/univer/pulls?q=is%3Apr+author%3Ajoaquimmj) in review.
- [TraceRoot](https://github.com/traceroot-ai/traceroot) (YC S25, 1.4k stars): five bugs in how it prices LLM calls. [Fix](https://github.com/traceroot-ai/traceroot/pull/2941) approved by the core team.

**Research**

[Filling the Gaps](https://github.com/joaquimmj/deskstack/blob/main/bench/paper/deskstack-bench.pdf) measures how often Claude misreports figures when it builds financial models. Across 300 runs on 50 companies, 3.5% of the figures it filed were wrong with web search alone, and 0 of 3,230 with data taken from the filings. Every flagged figure was checked by hand, the robustness test was pre-registered, and the [code and data](https://github.com/joaquimmj/deskstack/tree/main/bench) are public.

**Math**

- **OEIS** ([paper](https://github.com/joaquimmj/oeis-walnut/blob/main/paper/draft.pdf), [code](https://github.com/joaquimmj/oeis-walnut)): a 2017 conjecture of Clark Kimberling (A284364 to A284366) is false, first at n = 2,977,771, checkable in one line of integer arithmetic. Submitted to the OEIS, under review. The paper also proves the conjectures of twelve other entries (Walnut, hand proofs, exact computation) and corrects A284677, whose formula is off by one index from n = 6. Not refereed yet.
- **Erdős problems**, both still open. [#939](https://github.com/joaquimmj/erdos-939): no coprime 4-powerful solution of a + b = c up to 9·10^18, and no 5-powerful one up to 10^20 besides the two known. [#901](https://github.com/joaquimmj/erdos901): certified search (CEGAR with ILP and SAT, DRAT proofs checked by drat-trim) for 6-uniform hypergraphs without Property B below 147 edges; none found, and the 147-edge Abbott–Moser construction is verified edge-critical.

Open to founding, growth and engineering roles at early-stage startups, full-time or internship, in SF or remote from Paris. Reach me on [LinkedIn](https://www.linkedin.com/in/joaquimmanjijung/).
