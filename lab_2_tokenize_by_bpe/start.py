"""
BPE Tokenizer starter
"""

# pylint:disable=too-many-locals, unused-variable

from main import (
    collect_frequencies,
    decode,
    encode,
    get_vocabulary,
    load_vocabulary,
    train,
)


def main() -> None:
    """
    Launches an implementation
    """
    with open("lab_2_tokenize_by_bpe/assets/text.txt", "r", encoding="utf-8") as text_file:
        text = text_file.read()
    with open("lab_2_tokenize_by_bpe/assets/en_raw.txt", "r", encoding="utf-8") as text_file:
        text_reference_translation = text_file.read()
    with open("lab_2_tokenize_by_bpe/assets/en_encoded.txt", "r", encoding="utf-8") as text_file:
        translation_encoded_raw = text_file.read()
    with open(
        "lab_2_tokenize_by_bpe/assets/secrets/secret_1.txt",
        "r",
        encoding="utf-8"
    ) as text_file:
        secret_text = [int(x) for x in text_file.read().split()]
    with open("lab_2_tokenize_by_bpe/assets/ru_raw.txt", "r", encoding="utf-8") as text_file:
        ru_text = text_file.read()
    with open("lab_2_tokenize_by_bpe/assets/ru_encoded.txt", "r", encoding="utf-8") as text_file:
        ru_expected = [int(i) for i in text_file.read().split()]

    result = None

    freq_dict = collect_frequencies(text, None, "</s>")

    result = train(freq_dict, 100)
    if result is None:
        return None

    assert result, "Translation not working"

    return None

if __name__ == "__main__":
    main()
