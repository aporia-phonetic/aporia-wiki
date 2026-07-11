# rules_translator

*Source: `heterodyne/agents/rules_translator.py`*

agents/rules_translator.py

Translates Danger Signal game rulebooks (A.C.E.S., H.E.R.O., H.A.R.T., E.C.H.O.)
into target languages via the BatchDispatcher.

Usage (CLI / pipeline, no GUI):
    from agents.batch_dispatcher import BatchDispatcher
    from agents.rules_translator import RulesTranslator

    dispatcher = BatchDispatcher(api_key=..., model=...)
    translator = RulesTranslator(dispatcher)

    translated = translator.translate_rulebook(
        game_id="aces",
        rulebook_text=Path("documents/ACES rules (final w deck).pdf").read_text(),
        target_language="es",
    )
    Path("output/ACES_rules_es.md").write_text(translated)

    # Or translate all four games into multiple languages in one batch:
    results = translator.translate_all_games(
        game_texts={
            "aces": aces_text,
            "hero": hero_text,
            "hart": hart_text,
            "echo": echo_text,
        },
        target_languages=["es", "pt", "fr", "de"],
    )
    # results["es"]["aces"] -> translated markdown string

PDF extraction:
    These rulebooks are PDF-only. Extract text before passing in:
        import pdfplumber
        with pdfplumber.open("documents/ACES rules (final w deck).pdf") as pdf:
            text = "

".join(page.extract_text() or "" for page in pdf.pages)

    Or use pypdf:
        from pypdf import PdfReader
        reader = PdfReader("documents/ACES rules (final w deck).pdf")
        text = "

".join(page.extract_text() for page in reader.pages)

Output format:
    Translated rules are returned as markdown-formatted plain text.
    Same section structure as source. Tables preserved. Suit symbols preserved.
    Translator is instructed to note untranslatable game terms inline.

Cost estimate (Batch API, Sonnet 4.6):
    Single game, single language: ~$0.05–$0.15
    All 4 games × 6 languages = 24 requests: ~$1.20–$3.60 total

## Defined here

### `RulesTranslator`

Translates Danger Signal game rulebooks into target languages.

Uses the same BatchDispatcher as TranslationAgent but produces markdown
text output rather than JSON, because rulebooks are prose documents, not
structured episode data.

Args:
    dispatcher: Initialized BatchDispatcher instance.
