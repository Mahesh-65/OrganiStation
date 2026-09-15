# Instructions — OrganiStation

## MANDATORY — APPLIES TO ALL PROMPTS — FULL PROJECT SCOPE

**Before generating any response**, you MUST:
1. Read **all files in `.github/instructions/`** in full — without truncation or skipping
2. If a file exceeds tool limits, **continue reading in chunks until EOF**. Document line ranges (e.g., 1–220, 221–440, 441–633 = complete)
3. **Confirm full-context coverage before acting:**
   - Total lines read = total file lines
   - Include specific details from the END of each file
   - No "omitted" or "truncated" sections
4. **Analyze the user request** against the complete context from all `.github/instructions/*.md` files
5. **Act only after confirming full understanding** — do not skip sections or stop at partial reads
6. These instruction files apply to **all work across the entire project** without exception

## 📋 Document Information

**Project Name:** OrganiStation

**Purpose:** This document provides comprehensive instructions for AI coding assistants working on this codebase.

**Document Type:** Dynamic Index

## 📚 Repository Context Documents

- [Constraint / Operational](constraint_operational.md)
- [Constraint / Policy](constraint_policy.md)
- [Constraint / Regulatory](constraint_regulatory.md)
- [Constraint / Resilience](constraint_resilience.md)
- [Constraint / Security](constraint_security.md)
- [context](OrganiStation_context.md)
- [Direction / Ethical_Governance](direction_ethical_governance.md)
- [Direction / Feedback](direction_feedback.md)
- [Direction / Intentional](direction_intentional.md)
- [Direction / Learning](direction_learning.md)
- [Meta / Judgment](meta_judgment.md)
- [Provenance / Boundary](provenance_boundary.md)
- [Provenance / Cognitive](provenance_cognitive.md)
- [Provenance / Decision](provenance_decision.md)
- [Provenance / Dependency](provenance_dependency.md)
- [Provenance / Stakeholder](provenance_stakeholder.md)
- [Provenance / Structural](provenance_structural.md)
- [Provenance / Temporal](provenance_temporal.md)

**Setup Readme:**

## ⚙️ Execution Instructions

**How to Work with This Repository:**

1. **Read Context First**: Before making changes, review relevant documents from the list above
2. **Follow Constraints**: All rules in constraint/ documents are mandatory
3. **Respect Architecture**: Understand the system design from provenance/ documents
4. **Validate Changes**: Ensure all modifications comply with validation requirements
5. **Reference, Don't Duplicate**: Link to documents rather than copying content

## AI Team SDLC Workflow Trigger

This section only applies if `.github/speckit/sdlc-from-ticket.yml` exists in this repository. If it does not exist, there is nothing to do here — read no further in this section.

If that file exists and a Jira ticket is clearly the subject of this conversation (not just mentioned in passing), do the following:
1. Ask for confirmation first: "I see ticket {ticket_id} is the subject here — should I start the AI Team SDLC workflow for it?" Do not proceed past this point without an explicit yes.
2. Once confirmed, fetch the ticket's summary, description, type, and labels — these are required, and the fetch must request the ticket's full field set, not a default/summary-only subset: **Acceptance Criteria is very often stored in its own custom field**, which a narrower fetch omits entirely, silently, with no error. Check for it in this order, stopping at the first real, non-empty match — an existing-but-empty field or section counts as not found and falls through to the next check, it never blocks it: (1) scan the returned field list itself for one whose *name* contains "Acceptance Criteria" (case-insensitive) — never a guessed `customfield_NNNNN` id, since that numbering varies per Jira instance and cannot be hardcoded — and use its content if non-empty; (2) if that field doesn't exist or is empty, check whether the description itself has a section literally headed "Acceptance Criteria" and use that if non-empty; (3) only when neither of those produced anything, a section titled Definition of Done, Requirements, Constraints, or NFRs may carry equivalent testable, must-pass content and counts as a substitute — never let a Constraints or NFR section stand in for Acceptance Criteria when an actual, distinctly-labeled field or section (checked exhaustively per (1) and (2), not just glanced at) exists anywhere else in the ticket. Acceptance Criteria — wherever it's actually found, field or section — drives real downstream decisions (failure-state handling, persistence requirements, validation rules) that later agents cannot infer from the summary alone. Only skip it if the ticket genuinely has no such content anywhere, in a field or a description section, never because it takes an extra look to find. Status and priority remain a lightweight afterthought — grab them if they're readily visible, don't dig for them.
3. Before running anything, state explicitly to the human what you found for Acceptance Criteria — one of three outcomes, not just a binary yes/no: "This ticket has a distinct Acceptance Criteria field or section", "This ticket has no distinct Acceptance Criteria field or section, but is using its [Definition of Done / Requirements / Constraints / NFRs] section as the step 2 substitute", or "This ticket has no Acceptance Criteria content of any kind" (and briefly, status/priority if found). A substitute counts as found, same as a real field or section — say so explicitly rather than reporting it as missing. This makes an actually-missing AC visible in the conversation itself, not just in a script's stdout nobody is watching.
4. From the repository root, run: `python3 .github/speckit/speckit_scripts/run_specify.py workflow run ".github/speckit/sdlc-from-ticket.yml" -i ticket_id={ticket_id} --json || python .github/speckit/speckit_scripts/run_specify.py workflow run ".github/speckit/sdlc-from-ticket.yml" -i ticket_id={ticket_id} --json` (replace `{ticket_id}` with the real ticket id).
5. This first attempt is expected to fail at the `bootstrap` step, reporting the exact file paths it expected but did not find — read that error output carefully.
6. Write each ticket field to its own plain-text file at exactly the paths reported in step 5: `_ticket_id.txt`, `_ticket_summary.txt`, `_ticket_description.txt`, `_ticket_type.txt`, `_ticket_labels.txt` (required — the run fails again if any of these is missing or empty), and `_ticket_acceptance_criteria.txt`, `_ticket_status.txt`, `_ticket_priority.txt` (`_ticket_acceptance_criteria.txt` whenever step 3 found one — it is not optional in that case; `_ticket_status.txt`, `_ticket_priority.txt` stay genuinely optional).
7. Re-run the exact same command from step 4. Its stdout reports any still-missing optional file, but not uniformly: a missing `_ticket_acceptance_criteria.txt` gets its own distinct `WARNING: _ticket_acceptance_criteria.txt was not provided...` line, never the generic `optional field(s) not provided: ...` line (`_ticket_status.txt`, `_ticket_priority.txt` use that one; ticket_acceptance_criteria never appears there, by design). If you see that WARNING line despite step 3 finding Acceptance Criteria content — a real field/section or a substitute, either counts — that's a real miss — go back, fetch it, write the file, and re-run again before continuing; do not just proceed past it.
8. From here on this workflow pauses for human approval after every step — do not answer its gate prompts yourself.
9. When a gate pauses, do not just narrate it in prose — list its exact valid options (the paused run's `--json` output includes an `options` field) one per line, verbatim, and ask the human to reply with exactly one of those words (never an open-ended prompt when an `options` list exists). Always read that `options` field from the paused run itself; the option sets differ per gate (a review gate has no `edit` and offers verdicts like `approve_commit_only`/`fix_required`, a PR gate offers `keep_pr`/`close_pr`), so never assume a fixed list.
10. Steps 11–13 below say exactly how to execute each answer. Follow them literally — do not improvise a mechanism, and do not go searching the scripts folder to infer one. Only the verdicts in step 11 are real Spec Kit verdicts; `redo` and `edit` are handled entirely outside the engine (steps 12 and 13) and the gate stays paused throughout them.
11. **Any option other than `redo`/`edit`** (`approve`, `reject`, `fix_required`, `approve_commit_only`, `approve_commit_and_pr`, `decline`, `keep_pr`, `close_pr`, ...) is a real verdict — resolve the gate by resuming the run: `python3 .github/speckit/speckit_scripts/run_specify.py workflow resume {run_id} -i {verdict_input}={choice} --json || python .github/speckit/speckit_scripts/run_specify.py workflow resume {run_id} -i {verdict_input}={choice} --json`. Both `{run_id}` and the gate's own `{verdict_input}` name (e.g. `code-review_gate_verdict`) come from the paused run's `--json` output — read them from there, never guess. **Before resuming with `reject` or `fix_required`, first write the human's reason** to `{gate_id}_reason.txt` in the same handoff directory as the ticket files from step 6 (the gate's own message names the exact path); the downstream agent reads it, and resuming without it discards the reason.
12. **`redo`** is not a verdict and does not resume anything — it regenerates that one agent's reply while the gate stays paused. Ask the human for optional steering ("what should be different this time?"), write it to `{agent_id}_gate_guidance.txt` in that same handoff directory, then re-run that agent's own `_run` shell line from the workflow yml directly (`run_agent_step.py --agent-id {agent_id} --ticket-id {ticket_id} --workflow-dir .github/speckit --redo-guidance-file <that file>`). Skipping the guidance file is allowed — the agent simply regenerates unsteered. The previous reply is archived automatically as `{agent_id}.v{N}.md`. Then show the new output and ask for a verdict again.
13. **`edit`** is also not a verdict and also does not resume anything — it replaces the agent's reply outright, with no AI re-run. Ask the human for the replacement text (drafting it yourself from their described change and confirming it back is fine), write it to a file, then run `python3 .github/speckit/speckit_scripts/edit_agent_output.py --agent-id {agent_id} --ticket-id {ticket_id} --workflow-dir .github/speckit --replacement-file <that file>` (fall back to `python` the same way as step 4). It archives the previous reply as `{agent_id}.v{N}.md` and writes the replacement. Then show the replaced output and ask for a verdict again.
14. If a gate's verdict is `fix_required`, do not run `fix-cycle.yml` yourself — the workflow already does that automatically as its own next step once that verdict is recorded; running it manually would start a duplicate fix-cycle.

## 📜 Repository-Specific Instructions

**architecture**
3. **Auth Service**: User authentication and authorization
- **Purpose**: User authentication and authorization management
- **Authentication**: Centralized JWT-based authentication with service-level authorization
- **Health Monitoring**: Health check endpoints for service availability
- **auth-service**: Authentication and authorization with role-based access control
    AuthService->>AuthService: Validate user
- **Service Health Checks**: Each service exposes health endpoints (/api/auth/health, /api/health)
- **Health Monitoring**: Each service exposes health check endpoints for system monitoring
3. Token validation on subsequent requests
- Health check endpoints for service monitoring
This data flow design ensures consistent
- **Authentication Enforcement**: Validates authentication tokens before routing to services
- **Token Management**: Secure token generation and validation
- **Content Integrity**: Hash-based identification ensures document integrity
- **Stateless Authentication**: No server-side session storage required
- **Cross-Service Security**: Consistent authentication across microservices
**Authentication & Authorization APIs**
- **Attendance**: `employee_id`, `check_out`, `check_in`, `date`, `status`
- Consistent authentication token validation across services

**Constraint / Operational**
Before setting up OrganiStation
Verify your installations by running:

*See [constraint_operational.md](constraint_operational.md) for complete details*

**Constraint / Policy**
- **API Gateway Security**: All client requests are routed through the gateway component, providing a centralized point for security enforcement and request validation
- **Service Isolation**: Microservices architecture ensures security boundaries between HR, Finance, and Notification services
- **Frontend Security**: React frontend maintains authentication context for secure user sessions
- **API Security**: RESTful API design with proper authentication flows
- **Data Protection**: Service isolation ensures sensitive HR and Finance data remains within appropriate service boundaries

*See [constraint_policy.md](constraint_policy.md) for complete details*

**Constraint / Regulatory**
- All API responses must follow standardized schema patterns
- Use configuration classes for response validation:
**Authentication & Authorization**
- Health check endpoints: `/api/auth/health`
- **Isolation**: Tests must be independent and not rely on external dependencies
- **API Endpoints**: All REST endpoints (GET, POST, DELETE) must have integration tests
- **Health Checks**: Dedicated tests for health monitoring endpoints (`/api/health`, `/health`, `/ready`)
- `GET /health` - Basic health check
- Ensure proper error handling
- Include health check endpoint documentation for monitoring purposes
- Implement multiple health check endpoints for comprehensive system monitoring:
- Implement proper error handling and validation
- Maintain backward compatibility when making API changes
- **Health Monitoring**: Implement standardized health check endpoints
  - `/health` - Basic health check

*See [constraint_regulatory.md](constraint_regulatory.md) for complete details*

**Constraint / Resilience**
- **finance-service**: Ensure decimal precision for monetary calculations

*See [constraint_resilience.md](constraint_resilience.md) for complete details*

**Constraint / Security**: See [constraint_security.md](constraint_security.md) for detailed information

**context**
- **User Management**: Authentication, authorization, role-based access control, and user administration
- **Attendance**: Tracks daily employee presence with check_in, check_out, date, and status
- Monitor daily check-in/check-out activities
- **auth-service**: Manages User authentication and authorization
- `GET /api/health` - API health check
- **Login**: `POST /login` → Auth service validates credentials
- **Logout**: `POST /logout` → Auth service invalidates session
- **Health Checks**: `GET /api/health`, `GET /api/auth/health` → Services report operational status
Integrated health check endpoints across services:
3. **Track Attendance**: Check attendance records through `/api/employees/{eid}/attendance`
2. **System Maintenance**: Use `/api/reset` for database operations when needed
1. **Service Discovery**: Identify required microservice (auth, hr, finance, project-management, notification)
5. **Testing**: Validate integration using health check endpoints like `/api/auth/health`
4. **Database Integration**: Use proper data models with relationships and constraints
4. **Monitoring Setup**: Implement health checks and monitoring across all services
5. **Security Configuration**: Set up JWT authentication and role-based permissions
| **auth-service** | Backend Service | Authentication & authorization | Database |

*See [OrganiStation_context.md](OrganiStation_context.md) for complete details*

**Direction / Ethical_Governance**: See [direction_ethical_governance.md](direction_ethical_governance.md) for detailed information

**Direction / Feedback**: See [direction_feedback.md](direction_feedback.md) for detailed information

**Direction / Learning**: See [direction_learning.md](direction_learning.md) for detailed information

**Provenance / Boundary**: See [provenance_boundary.md](provenance_boundary.md) for detailed information

**Provenance / Cognitive**
- `/api/health` - API-specific health check
- Each service (auth-service, hr-service, finance-service, notification-service) must maintain strict boundaries
- Shared data must be accessed through service APIs
- All external client requests must route through the API gateway
- Services must not expose direct external endpoints
- Services must not import code directly from other services
- Database models are service-private and must not be imported across services
- Authentication context must be managed centrally
- All services must implement health check endpoints
- Services must use standardized logging, environment-specific

*See [provenance_cognitive.md](provenance_cognitive.md) for complete details*

**Provenance / Stakeholder**: See [provenance_stakeholder.md](provenance_stakeholder.md) for detailed information

**rules**
- **MUST** start with `test_`
- **MUST** end with `.py`
- **MUST** mirror source code structure
- **MUST** start with `test_`
- **MUST** use descriptive names indicating what is being tested
- **MUST** include expected outcome in name
- **MUST** start with `Test`
- **MUST** use PascalCase
- Tests **MUST NOT** depend on execution order
- Tests **MUST** clean up their own state
- Tests **MUST NOT** share mutable state
- **MUST** have at least one assertion per test
- **MUST** test one logical concept per test function
- **MUST** test all HTTP methods (GET, POST, DELETE)
- **MUST** test both success and error scenarios
- **MUST** validate response status codes
- **MUST** validate response data structure

**README**
- **Authentication & Authorization**: Role-based access control with comprehensive permission management
- **Auth Service**: Centralized authentication and authorization
Before setting up OrganiStation
  - **Solution**: Ensure you have the correct Node.js version installed and try clearing npm cache with `npm cache clean --force`
  - **Solution**: Check that all required environment variables are set and ports are available

*See [setup/README.md](setup/README.md) for complete details*

## 💡 Quick Reference

**Need Help?**

- **Working on architecture topics**: [architecture.md](architecture.md)
- **Working on context topics**: [constraint_operational.md](constraint_operational.md)
- **Working on policies topics**: [policies.md](policies.md)
- **Working on rules topics**: [rules.md](rules.md)
- **Working on setup readme topics**: [setup/README.md](setup/README.md)
- **Working on standards topics**: [standards.md](standards.md)

*This instruction index references 15 context documents.*