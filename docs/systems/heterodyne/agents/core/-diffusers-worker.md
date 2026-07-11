# _diffusers_worker

*Source: `heterodyne/agents/_diffusers_worker.py`*

agents/_diffusers_worker.py

Standalone text-to-image worker for the ImageAgent DIFFUSERS backend.

Run by ImageAgent via the isolated `.venv-imagegen` interpreter (which carries
its own torch/diffusers, incompatible with the main venv's voice stack — see
docs / memory: image-gen-setup). It is invoked as a script, NOT imported as
part of the `agents` package, so it must not import anything from `agents`.

Protocol:
    stdin  : one JSON object (the spec — see KEYS below)
    stdout : one JSON object on success: {"ok": true, "path", "seconds", "vram_gb"}
             on failure: {"ok": false, "error"}  (and exit code 1)

Spec keys:
    model            HF model id or local path (AutoPipeline-compatible)
    prompt           positive prompt
    negative_prompt  negative prompt (ignored by models that don't support it)
    width, height    ints, must be multiples of 8
    steps            num_inference_steps
    guidance         guidance_scale
    seed             int or null
    out_path         absolute path to write the PNG
    # ── optional character identity (single-subject shots) ──
    identity_ref     path to a reference face image (e.g. the portrait bust)
    identity_scale   0.0-1.0 IP-Adapter strength (default 0.65)
    identity_kind    "ipadapter_faceid" | "none" (default none)
    ip_adapter_dir   dir holding ip-adapter-faceid_sdxl.bin (default models/ip_adapter)
    lora_path        path to a trained character LoRA (.safetensors) or None
    lora_scale       0.0-1.0 LoRA strength (default 0.8)

All identity/LoRA features are guarded: any missing weight/dep or detection
failure logs to STDERR and falls back to a plain txt2img render — a batch is
never hard-failed by identity.

## Top-level functions

- **`main()`** — 
