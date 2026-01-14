# Infrastructure Operations - Agent Instructions

**Classification**: T4b - Infrastructure & Procedural Agent Documentation  
**Domain**: Infrastructure Operations  
**Version**: 1.0  
**Status**: ACTIVE  
**Effective Date**: 2025-11-25  
**Next Review**: 2026-02-25  
**Owner**: System Architect

---

## Document Sections

This instruction set contains the following sections:

- Introduction
- Authority Matrix
- Procedures
- Machine-Readable Policy

---

*This document is auto-generated from the canonical JSON source: `infrastructure/AGENT_INSTRUCTIONS.json`*  
*Content Hash: -715700941109346319*
    - Create a new directory for the module under `infrastructure/modules/` (e.g., `secure-s3-bucket`).
    - Implement the core logic in `main.tf`.
    - **Add a `README.md`**: This is mandatory. The README must contain:
        - A description of what the module does.
        - All input variables and their purpose.
        - All outputs.
        - A clear example of how to use the module.

3. **Implement Versioning and Tagging**:
    - Add a `versions.tf` file to pin the required Terraform and provider versions.
    - Ensure all resources created by the module are tagged with the module's name and version for traceability.

4. **Write Tests and Examples**:
    - Create an `examples/` directory within the module folder.
    - Provide at least one working example of how to instantiate the module.
    - Use a simple test framework or a separate Terraform configuration to provision and destroy the module's resources to ensure it works as expected.

5. **Submit for Review**:
    - Open a Pull Request. An **L3 (Senior Dev)** must review the module for:
        - **Correctness**: Does it provision the correct resources?
        - **Security**: Does it follow the principle of least privilege? Are resources secure by default?
        - **Reusability**: Is it generic enough to be used in different contexts?
        - **Documentation**: Is the `README.md` clear and complete?

### Procedure 3: Manage Terraform State

**When**: A high-risk operation is required that directly manipulates the Terraform state file, such as importing an existing resource or resolving state drift. These operations are dangerous and require architect-level approval.

**Steps**:

1. **Emergency and Approval**:
    - State manipulation is an emergency-only procedure. It should never be part of a standard workflow.
    - Obtain explicit approval from an **L4 (Architect)** before proceeding. The justification must be documented in a GitHub issue.

2. **Backup the State**:
    - Before any operation, manually create a backup of the remote state file. The remote backend (e.g., S3 bucket) should have versioning enabled, but a manual backup provides an extra layer of safety.

3. **Use a Dedicated, Locked Workspace**:
    - Perform the state operation on a clean, isolated machine or container.
    - Ensure state locking is active to prevent anyone else from running `apply` while you are manipulating the state.

4. **Execute the State Command**:
    - Use the appropriate `terraform state` subcommand (e.g., `mv`, `rm`, `replace-provider`).
    - **For `terraform import`**:
        - Write the resource configuration block in your `.tf` code first.
        - Run `terraform import <RESOURCE_ADDRESS> <RESOURCE_ID>`.
        - Run `terraform plan` immediately after to verify that Terraform now sees the imported resource as being under its control and that there are no differences.

5. **Verify and Document**:
    - After the operation, run `terraform plan` to confirm the state file accurately reflects the desired reality and that no further changes are planned.
    - Document the entire procedure, including the commands run and the reasons for the operation, in the corresponding GitHub issue.

---

### Procedure 4: Handle Infrastructure Security Scans

**When**: A security vulnerability is detected in the IaC code, either by the automated CI pipeline scanner or a manual audit.

**Steps**:

1. **Automated Scanning in CI**:
    - The CI pipeline is configured to run a static analysis security scanner (e.g., `tfsec`, `checkov`) on every Pull Request that modifies `.tf` files.
    - The pipeline will fail if any **CRITICAL** or **HIGH** severity vulnerabilities are detected.

2. **Triage and Prioritize Findings**:
    - Review the scanner's output in the failed CI job.
    - **CRITICAL/HIGH**: These must be remediated immediately. The PR cannot be merged until they are fixed.
    - **MEDIUM/LOW**: Create a GitHub issue to track the finding. These should be addressed in a timely manner but do not block the merge unless they violate a specific policy.

3. **Remediate the Vulnerability**:
    - Modify the IaC code to fix the issue. This often involves:
        - Applying more restrictive IAM policies.
        - Closing open ports in security groups.
        - Enabling encryption or logging on resources.
    - Push the fix to the PR branch. The CI pipeline will re-run, and the scan should now pass.

4. **Handling False Positives**:
    - If a finding is determined to be a false positive, you must explicitly ignore it.
    - Add a comment directly above the resource in the `.tf` file (e.g., `#tfsec:ignore:aws-s3-enable-bucket-logging`).
    - The comment must include a clear justification for why the finding is being ignored. This creates an auditable record.

5. **Regular Audits**:
    - In addition to PR scans, a full scan of the `main` branch is run on a weekly schedule.
    - This process ensures that new vulnerability definitions from the scanner are applied to the existing codebase and helps catch anything that might have been missed. Any findings from this audit are tracked as new GitHub issues.

---

## 4. Quick Decision Tree

Use this tree to determine the correct procedure for common tasks.

- **Is the task a change to existing infrastructure?**
  - **YES**: Go to **Procedure 1: Plan and Apply Infrastructure Changes**.
- **Is the task creating a new, reusable component?**
  - **YES**: Go to **Procedure 2: Create a Reusable IaC Module**.
- **Does the task involve `terraform state` commands or importing resources?**
  - **YES**: Go to **Procedure 3: Manage Terraform State**. This is a high-risk operation.
- **Is the task related to checking for security vulnerabilities?**
  - **YES**: Go to **Procedure 4: Handle Infrastructure Security Scans**.

---

## 5. CIDS Edge Node Protection (Critical)

**Incident Reference:** `INC-CIDS-20251209-001` — A rogue agent stopped critical network services, causing full secured network outage.

The CIDS Edge Router (`203.0.113.10`) is a CRITICAL infrastructure component. The following operations are **PROHIBITED** without explicit joediggidyyy approval:

### 5.1 Prohibited Actions

| Action | Risk Level | Consequence |
|--------|------------|-------------|
| `systemctl stop cids-killswitch` | **CRITICAL** | Full secured network outage |
| `systemctl stop hostapd` | **CRITICAL** | AP goes down, all clients disconnected |
| `systemctl stop dnsmasq` | **HIGH** | No DHCP, clients can't get IPs |
| `ip route del ... table 200` | **CRITICAL** | VPN routing broken |
| `ip route flush table 200` | **CRITICAL** | VPN routing broken |
| `iptables -F` (flush rules) | **CRITICAL** | Firewall disabled, security breach |
| Deleting files in `/etc/codesentinel/cids/` | **HIGH** | Configuration loss |
| Modifying `/etc/hostapd/hostapd.conf` | **HIGH** | AP misconfiguration |
| Stopping NordVPN or `nordlynx` interface | **CRITICAL** | VPN tunnel down |

### 5.2 Pre-Approved Safe Operations

These operations are safe and agents may perform them:

- `systemctl status <service>` — Check service status
- `journalctl -u <service>` — View service logs
- `ip route show table 200` — Inspect routing (read-only)
- `iptables -L` — List firewall rules (read-only)
- `hostapd_cli -i wlx289401b13bec all_sta` — List connected clients
- `cat /var/lib/misc/dnsmasq.leases` — View DHCP leases
- Deploying new CIDS dashboard code (with proper testing)
- Updating whitelist files (with backup)

### 5.3 Emergency Recovery Commands

If an agent needs to restore network connectivity:

```bash
# 1. Restore VPN routing (if table 200 is empty)
sudo ip route add default dev nordlynx table 200
sudo ip route flush cache

# 2. Restart critical services
sudo systemctl restart cids-killswitch
sudo systemctl restart hostapd
sudo systemctl restart dnsmasq

# 3. Verify
ip route show table 200  # Should show: default dev nordlynx
systemctl is-active cids-killswitch  # Should show: active
```

### 5.4 Diagnostic Scripts

Use these pre-approved diagnostic scripts instead of ad-hoc commands:

| Script | Purpose |
|--------|---------|
| `tools/codesentinel/ops/cids_network_block_diagnostics.py` | Full network diagnosis |
| `tools/codesentinel/ops/cids_ap_diagnostics.py` | AP/WiFi diagnosis |
| `tools/codesentinel/ops/edge_killswitch_manager.ps1` | Killswitch status check |

---

## 6. Validation Checklist

Before submitting any infrastructure-related Pull Request, ensure it meets these criteria.

**Code Quality**:

- [ ] `terraform fmt -recursive` has been run.
- [ ] `terraform validate` passes.
- [ ] Variables and outputs are well-documented.
- [ ] No hardcoded secrets or sensitive values.
- [ ] Code is modular and follows DRY principles.

**Security**:

- [ ] `tfsec` or equivalent scan passes with no CRITICAL/HIGH findings.
- [ ] IAM policies follow the principle of least privilege.
- [ ] Security groups are restrictive and expose no unnecessary ports.
- [ ] Data is encrypted at rest and in transit.
- [ ] Logging and monitoring are enabled for all resources.

**Documentation**:

- [ ] PR description clearly explains the "what" and "why" of the change.
- [ ] `terraform plan` output is included in the PR.
- [ ] Any new modules have a `README.md` with usage examples.
- [ ] Complex logic is commented in the code.

**Compliance**:

- [ ] Changes adhere to global policies (e.g., `POLICY.md`).
- [ ] Resources are tagged according to the organization's tagging policy.
- [ ] The change does not violate any compliance frameworks (e.g., SOC2, GDPR).

---

## 6. Q&A / Common Questions

**Q: What should I do if `terraform plan` shows unexpected changes?**

**A**: Do NOT apply the plan. Investigate the root cause. It could be due to a provider update, manual changes in the cloud console (state drift), or incorrect code. Re-run the plan until it shows only the intended changes.

**Q: How do I manage secrets like API keys or database passwords?**

**A**: Use a dedicated secrets management tool like HashiCorp Vault or AWS Secrets Manager. Terraform should reference these secrets, not store them in state or version control.

**Q: Can I make a "quick fix" in the cloud console?**

**A**: No. All changes must go through the IaC workflow. Manual changes create state drift, are not peer-reviewed, and are not auditable. If an emergency fix is required, it must be immediately followed by a PR to codify the change.

**Q: What's the difference between a module and a resource?**

**A**: A resource is a single infrastructure object (e.g., an AWS S3 bucket). A module is a collection of resources that are used together to create a reusable component (e.g., a module to create a secure S3 bucket with logging and encryption).

**Q: How do we handle provider updates?**

**A**: Provider updates should be handled cautiously in a separate PR. Run `terraform plan` after updating the provider version to check for any breaking changes. Apply to staging first and run a full suite of integration tests.

---

## 7. References

This satellite is the **single source of truth** for infrastructure operations.

**Policy & Governance**:

- Global Policy: `POLICY.md`
- Document Classification: `DOCUMENT_CLASSIFICATION.md`
- Agent Instruction Strategy: `AGENT_INSTRUCTION_STRATEGY.md`

**Tools & Documentation**:

- Terraform: <https://www.terraform.io/docs>
- tfsec: <https://github.com/aquasecurity/tfsec>
- Checkov: <https://www.checkov.io/>

**CodeSentinel References**:

- Repository: <https://github.com/joediggidyyy/CodeSentinel>
- Deployment Satellite: `deployment/AGENT_INSTRUCTIONS.md`
- GitHub Satellite: `github/AGENT_INSTRUCTIONS.md`
