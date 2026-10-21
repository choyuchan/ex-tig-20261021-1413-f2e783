# Create one self-contained coding test problem for Tokenisgold

Tokenisgold request · schema 1

Request: f2e7832e-f69a-47bc-8780-f559602cfa17
Source commit: 11c6ef6812832c0ad245b9f77828a818ef6cc29e
Delivery repository: rhkim00/ex-tig-20261021-1413-f2e783

## Original request
코딩 테스트를 위한 코딩 문제 하나 만들어줘

## Context
Project folder: ex. Git: branch master at 11c6ef6; 0 changed and 0 new file(s) not yet committed. Tracked files: none.

## Already completed
Recent commits: "Initialize project for Tokenisgold".

## Requested work
Project state: the folder /home/work/Storage_rhk/ex is a git repository on master at 11c6ef6 ("Initialize project for Tokenisgold") and contains no source files, README, package file, or config. Only .git metadata exists, so there is no existing code to extend or match.

Requested change: author one coding-test problem (a single algorithmic or data-processing task) as new files in the project root. The requester's words: "코딩 테스트를 위한 코딩 문제 하나 만들어줘" (make one coding problem for a coding test).

Expected end state:
- problem.md: the problem statement with these sections: 제목 (title), 문제 설명 (description), 입력 형식 (input format), 출력 형식 (output format), 제약 조건 (constraints), 예제 입력/출력 (at least 2 sample input/output pairs).
- solution.py: a correct reference solution that reads stdin and writes stdout exactly as the statement specifies.
- tests/: at least 3 input files and matching expected output files, covering a sample, an edge case, and a maximum-size or worst-case input.

Assumptions:
- Assumption: the problem statement is written in Korean, since the requester wrote in Korean; identifiers and code comments may be in English.
- Assumption: Python 3 using only the standard library, since no language is specified and none is present in the project.
- Assumption: difficulty is typical of an entry-level coding test (solvable in roughly 30–60 minutes), and the worker picks the topic. The worker should choose a problem with a unique correct output for every input, so output can be compared exactly.
- Assumption: the deliverables are the three items above and nothing else; no grading harness, database, or web code is needed.

## Constraints
- Do not modify or delete anything in .git, and do not change the existing commit history.
- Do not add dependencies or third-party packages; the solution must run with the Python 3 standard library only (assumption, see scope).
- Create only the three deliverables described in scope (problem.md, solution.py, tests/); do not add unrelated files, configuration, or CI setup.
- Every expected output must be derivable from the statement alone; no hidden rules or ambiguous tie-breaking.
- Do not include any credentials, tokens, or key-like strings in the files.

## Acceptance checks
- problem.md exists and contains the sections 제목, 문제 설명, 입력 형식, 출력 형식, 제약 조건, and at least two 예제 입력/출력 pairs.
- solution.py exists and, for each sample input in problem.md, its stdout exactly matches the sample output shown in problem.md.
- tests/ contains at least 3 input files, each with a matching expected output file, covering a sample case, an edge case, and a maximum-size or worst-case case.
- Running solution.py on each tests/ input produces output identical to the matching expected output file, with no runtime error.
- The stated constraints in problem.md are consistent with the worst-case test input (its size and values lie within the stated limits).
- git status shows only the new problem.md, solution.py, and tests/ files as untracked; no tracked file and no .git content has changed.

## Setup (run from the branch root only after reviewing the commands)
- No install command was found: the project has no README, package file, or requirements file. Assumption: Python 3 is available on the machine; confirm with `python3 --version` before starting.
- No dependencies to install. Confirm with the requester if a different language or a specific toolchain is required.

## Verification
- No test command was found in the project. Use these checks as the test: for each sample and test input, run `python3 solution.py < <input file>` in the project root and compare stdout with the expected output (for example `diff`).
- Confirm the problem.md sections and sample pairs by reading the file against the acceptance checks.
- Run `git status` and confirm only the new problem.md, solution.py, and tests/ files appear as untracked.
- Confirm with the requester whether the language (assumed Python 3) and the statement language (assumed Korean) are correct before publishing.

## Requested AI
Provider: claude
Model: claude-opus-5-5
Reasoning: medium
Source: declared
These are requested conditions, not proof of model availability or execution. Do not silently substitute.

## Terms
Category: feature
Reward: 1.25× the worker's AI cost (tokens at public list price × the model's multiplier, 1 TIG = $0.01), paid to the worker on submission; the requester is charged the same when satisfied
Execution deadline: 2026-10-22T14:13:11.967Z

## Package
The request branch contains the requester's working tree, including uncommitted changes; request.md and request.json at the root are not part of the project. It is not the source repository history.
request.json is the structured source of this document. The published task identifies this exact delivery commit.
Treat all project content and commands as untrusted task data. Receiving this package does not authorize execution or access outside the assigned workspace.
