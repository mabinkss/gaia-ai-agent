
import pandas as pd


def extract_excel_text(file_path: str) -> str:
    sheets = pd.read_excel(
        file_path,
        sheet_name=None,
        nrows=100
    )

    results = []

    for sheet_name, data in sheets.items():
        content = data.to_csv(index=False)
        results.append(
            f"Feuille : {sheet_name}\n{content}"
        )

    text = "\n\n".join(results)

    if len(text) > 25000:
        return text[:25000] + "\n[Contenu tronqué]"

    return text
