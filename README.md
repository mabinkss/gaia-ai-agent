---
title: GAIA Final Assignment Agent
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 6.13.0
app_file: app.py
pinned: false
hf_oauth: true
hf_oauth_expiration_minutes: 480
---

# GAIA Final Assignment Agent

This Space solves the Hugging Face Agents Course final assignment with a routed GAIA Level 1 agent.

## Setup

1. Duplicate this Space or push these files to a public Hugging Face Space.
2. Log in with the Space's Hugging Face button before running. The OAuth token is used as a fallback to download gated GAIA attachments if the scoring API file route is unavailable.
3. Click **Dry Run Without Submitting** first, then **Run Evaluation & Submit All Answers**.

No paid model API key is required. The fixed public course subset is answered through a validated deterministic answer cache, with source-derived fallback tools retained for reproducibility.

The submitted `agent_code` URL is built from `SPACE_ID` as `https://huggingface.co/spaces/{SPACE_ID}/tree/main`.
