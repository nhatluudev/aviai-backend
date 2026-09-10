# src/agent/config.py
import os

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "val")
LLM_MODEL = os.getenv("RMIT_VAL_MODEL", "openai-gpt-5.2")
# Val's OpenAI-compatible base — keep the trailing slash, there is no /v1.
LLM_BASE_URL = os.getenv("RMIT_VAL_BASE_URL", "https://val.rmit.edu.au/api/")
LLM_API_KEY = os.getenv("RMIT_VAL_API_KEY")

TTS_VOICE = os.getenv("TTS_VOICE", "cosette")
TTS_PROVIDER = os.getenv("TTS_PROVIDER", "pocket")
OPENROUTER_TTS_MODEL = os.getenv("OPENROUTER_TTS_MODEL", "deepgram/aura-2")
OPENROUTER_TTS_SAMPLE_RATE = int(os.getenv("OPENROUTER_TTS_SAMPLE_RATE", "24000"))

# "openrouter-audio" provider: a single fixed speaker voice with real style/emotion
# instructions (unlike aura-2, which only supports swapping to a different persona).
OPENROUTER_AUDIO_MODEL = os.getenv("OPENROUTER_AUDIO_MODEL", "openai/gpt-audio-mini")

STT_PROVIDER = os.getenv("STT_PROVIDER", "faster_whisper")
OPENROUTER_STT_MODEL = os.getenv("OPENROUTER_STT_MODEL", "openai/whisper-large-v3")

# LLM_PROVIDER="lmstudio"
# LLM_MODEL="qwen/qwen3-vl-8b"
# LLM_BASE_URL="hhttp://localhost:1234/v1"