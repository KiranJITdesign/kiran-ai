# Third-party notices

KiranAI creator and integration author: S Kiran.

## SmolLM

The language foundation is HuggingFaceTB/SmolLM-135M-Instruct by Hugging Face.
Source: https://huggingface.co/HuggingFaceTB/SmolLM-135M-Instruct

The original locally available Q4_0 GGUF has SHA-256
`eb2c714d40d4b35ba4b8ee98475a06d51d8080a17d2d2a75a23665985c739b94`.
Its accompanying license is included as `kiran_ai/assets/LICENSE-SMOLLM`.
Upstream weights retain Apache License 2.0. KiranAI's output manifest identifies
any merged modifications, which are not a new from-scratch foundation model.
KiranAI-specific modifications follow the root LICENSE without revoking upstream
rights. Original tokenizer and model provenance metadata are retained.

## Open-JEV

The unmodified reference file is vendored from Kye Gomez's Open-JEV repository:
https://github.com/kyegomez/open-jev
Revision: `93843ef288f3d35fd91263377c40b6f917d77da0`.

See `kiran_ai/vendor/open_jev/LICENSE` and `NOTICE.md`. It is an unofficial
research reconstruction, not TypeSafe AI's trained product. KiranAI's small
operation-policy checkpoint, if included, was trained locally on synthetic
structured records and has only the scope stated in its model card.

## Runtime dependencies

llama-cpp-python and llama.cpp supply GGUF inference under their respective
upstream licenses. PyTorch, NumPy and training-only libraries retain their own
licenses. These are runtime/tooling dependencies; no model service is required
by the local chat backend.
