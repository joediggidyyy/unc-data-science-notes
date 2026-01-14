# KMS signing providers for policy enforcement

## Metadata

| Field | Value |
| --- | --- |
| Document Title | kms signing |
| Domain / Scope | DOC |
| Artifact Type | Document |
| Classification | Internal |
| Execution Window | 2025-11-26 |
| Operator / Author | ORACL-Prime |
| Location | CodeSentinel/docs/guides/kms_signing.md |

---


The project's policy signing path supports multiple signing providers. This guide explains how to configure AWS KMS and Azure Key Vault CLI-based providers as an interim production option.

Important: using CLI-based signing means the runner executing the signing command must have appropriate permissions and CLI tooling installed (aws / az). For higher-confidence deployments, prefer SDK-backed signing with proper CI secret handling and key rotation.

Provider options and environment configuration

- POLICY_SIGNING_PROVIDER: Selects the provider type. Supported values (this repo) – `kms` (simulated), `aws_kms`, `azure_kv`, or leave empty to use local HMAC or raw SHA fallback.

AWS KMS (CLI)

- Set POLICY_SIGNING_PROVIDER=aws_kms

- Set POLICY_AWS_KMS_KEY to a KMS key ID/ARN (e.g., arn:aws:kms:us-west-2:111:key/abcd)

- Ensure `aws` CLI is installed and configured with credentials that can call `kms sign`.

SDK-backed AWS KMS (recommended for CI)

- Set POLICY_SIGNING_PROVIDER=aws_kms_sdk
- Set POLICY_AWS_KMS_KEY to a KMS key ID/ARN
- Ensure the runner has boto3 installed and credentials (via environment or instance role) with permission to call kms:Sign

Example GitHub Actions snippet (SDK-backed):

```yaml
- name: Install requirements (for signing)
  run: pip install -r requirements-dev.txt

- name: Persist signed audit (CI runner)
  env:
    POLICY_SIGNING_PROVIDER: aws_kms_sdk
    POLICY_AWS_KMS_KEY: ${{ secrets.AWS_KMS_KEY }}
    AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
    AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    AWS_DEFAULT_REGION: us-west-2
  run: |
    python -c "from codesentinel.utils.policy_enforcer import _persist_signed_event; import tempfile; sm=''; print('dry')"
```

Azure Key Vault (CLI)

- Set POLICY_SIGNING_PROVIDER=azure_kv

- Set POLICY_AZURE_KV_NAME to the vault name and POLICY_AZURE_KV_KEY to the key name

- Ensure `az` CLI is installed and logged in with access to the key (az keyvault key sign)

Behavior and fallback

- If the selected CLI tool is missing or the sign call fails, the signer will raise a RuntimeError.

- In absence of any provider or signing key, the system falls back to HMAC-SHA256 (POLICY_SIGNING_KEY) or raw SHA256 digest.

Security notes and recommendations

- CLI-driven signing is an operationally practical step for bridging local admin environments and early production systems, but should not be considered a long-term substitute for crypto-backed signing using secure key material and hardware modules (HSMs/TPM).

- For production CI, prefer SDK-backed KMS integration and ensure keys are stored in the platform's secret store (GitHub Actions Secrets, Azure Key Vault, or AWS Secrets Manager), and use minimal-scope principals and key-rotation policies.

Next steps (recommended)

- Add an SDK-backed provider using boto3 or azure-keyvault that avoids external process calls and can be unit-tested with standard mocking.

- Add CI runner policies or gating so only authorized runners can perform KMS signing operations at pipeline time.
