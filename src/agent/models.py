"""
Singleton module for pre-loaded ML models (TTS, STT).
Models are loaded once at app startup to avoid delays during WebSocket connections.
"""

from rich.console import Console
from agent.config import (
    TTS_PROVIDER,
    TTS_VOICE,
    OPENROUTER_TTS_MODEL,
    OPENROUTER_TTS_SAMPLE_RATE,
    OPENROUTER_AUDIO_MODEL,
    STT_PROVIDER,
    OPENROUTER_STT_MODEL,
)

console = Console()

# Global model instances
_tts_instance = None
_stt_instance = None


def get_tts_style_instructions(voice_instructions: str) -> str | None:
    """Pass the LLM's free-form voice_instructions through as delivery style, if the
    active TTS provider actually follows style instructions (openrouter-audio).
    Other providers (aura-2, pocket) only accept a fixed voice name here, so a
    free-text string would break them.
    """
    if TTS_PROVIDER != "openrouter-audio":
        return None
    return voice_instructions


def init_models():
    """Initialize TTS and STT models. Call this at app startup."""
    global _tts_instance, _stt_instance

    console.print("[cyan]Loading TTS model...[/cyan]")
    if TTS_PROVIDER == "pocket":
        from agent.io.tts.tts_pocket import TextToSpeechService
        _tts_instance = TextToSpeechService(voice=TTS_VOICE)
    elif TTS_PROVIDER == "openrouter":
        from agent.io.tts.tts_openrouter import TextToSpeechService
        _tts_instance = TextToSpeechService(
            voice=TTS_VOICE,
            model=OPENROUTER_TTS_MODEL,
            sample_rate=OPENROUTER_TTS_SAMPLE_RATE,
        )
    elif TTS_PROVIDER == "openrouter-audio":
        from agent.io.tts.tts_openrouter_audio import TextToSpeechService
        _tts_instance = TextToSpeechService(
            voice=TTS_VOICE,
            model=OPENROUTER_AUDIO_MODEL,
            sample_rate=OPENROUTER_TTS_SAMPLE_RATE,
        )
    else:
        raise ValueError(f"Unsupported TTS_PROVIDER: {TTS_PROVIDER}")
    console.print("[green]✓ TTS model loaded[/green]")

    console.print("[cyan]Loading STT model...[/cyan]")
    if STT_PROVIDER == "faster_whisper":
        from agent.io.stt.faster_whisper import FasterWhisperSTT
        _stt_instance = FasterWhisperSTT(
            model_size="small",
            silence_db=-45,
            end_silence_sec=1.2,
        )
    elif STT_PROVIDER == "openrouter":
        from agent.io.stt.openrouter_stt import OpenRouterSTT
        _stt_instance = OpenRouterSTT(model=OPENROUTER_STT_MODEL)
    else:
        raise ValueError(f"Unsupported STT_PROVIDER: {STT_PROVIDER}")
    console.print("[green]✓ STT model loaded[/green]")


def get_tts():
    """Get the shared TTS instance."""
    if _tts_instance is None:
        raise RuntimeError("TTS model not initialized. Call init_models() first.")
    return _tts_instance


def get_stt():
    """Get the shared STT instance."""
    if _stt_instance is None:
        raise RuntimeError("STT model not initialized. Call init_models() first.")
    return _stt_instance
