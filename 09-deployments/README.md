# 09-deployments — release state

Development, staging and production environments live here as configuration
and deployment records.

This layer answers four questions:

1. What version is running?
2. In which environment is it running?
3. How was it released and verified?
4. How can it be rolled back safely?

Do not store credentials here. Secrets stay in `.env` or an approved secret
manager. Keep reusable build logic in `03-engineering-os/` or `07-scripts/`;
this layer records environment-specific release state.

## Structure

No deployments yet — this layer is a documented convention, not populated dirs.
When real releases exist, organise them so environment and ownership are
explicit:

```
09-deployments/
├── internal/                 Own infra (the machines this OS runs on): gateway, cron, n8n, git host
│   └── <service>/RELEASE.md   version, host, how released, rollback
└── clients/                  Per-client deployments (mirrors 06-clients/)
    └── <client>/<env>/RELEASE.md   dev | staging | prod release records
```

- **Client deployments** get a subfolder per client, then per environment —
  the same client boundary as `06-clients/`. If a client deployment record
  contains sensitive detail (hostnames, endpoints, account IDs), gitignore that
  client's subfolder the way `06-clients/` is gitignored; keep only a redacted
  `RELEASE.md` stub in git, or exclude it entirely.
- **Internal deployments** (this OS's own infra) are non-sensitive release
  state and can stay in git.
- One `RELEASE.md` per deployment answers the four questions above (what
  version, which env, how released/verified, how to roll back).
