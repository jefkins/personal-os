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
